"""
CipherSearch Core Engine
========================
Implements Searchable Symmetric Encryption (SSE):
- AES-256-GCM for document encryption
- HMAC-SHA256 for deterministic search token generation
- PBKDF2 for key derivation from master password
- SQLite-backed encrypted index for server-side storage

Security model: The SecureServer class NEVER receives keys or plaintext.
"""

import os
import re
import hmac
import json
import time
import hashlib
import base64
import sqlite3
from datetime import datetime
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, field
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class EncryptedDocument:
    """What the server receives — no plaintext anywhere."""
    doc_id: str
    encrypted_content: str  # base64-encoded AES-GCM ciphertext
    nonce: str  # base64-encoded 96-bit nonce
    tokens: List[str]  # HMAC-SHA256 search tokens (opaque to server)
    keyword_count: int
    timestamp: str


@dataclass
class SearchResult:
    """Encrypted search result returned by server."""
    doc_id: str
    encrypted_content: str
    nonce: str


# ---------------------------------------------------------------------------
# Client-Side Encryption Engine
# ---------------------------------------------------------------------------

class CipherSearchEngine:
    """
    CLIENT-SIDE encryption engine.
    This class holds the master keys and performs ALL crypto operations.
    In a real deployment, this runs in the user's browser or local machine.
    The keys NEVER leave this class / the client environment.
    """

    STOP_WORDS = frozenset({
        'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had',
        'her', 'was', 'one', 'our', 'out', 'has', 'have', 'been', 'some', 'them',
        'than', 'its', 'over', 'also', 'with', 'this', 'that', 'from', 'they',
        'will', 'each', 'make', 'like', 'long', 'look', 'many', 'then', 'what',
        'were', 'when', 'your', 'said', 'into', 'who', 'did', 'get', 'may', 'him',
        'his', 'how', 'let', 'say', 'she', 'too', 'use', 'more', 'other', 'could',
        'would', 'should', 'being', 'after', 'before', 'between', 'through',
        'during', 'without', 'again', 'further', 'once', 'here', 'there', 'where',
        'why', 'very', 'just', 'only', 'own', 'same', 'both', 'few', 'most', 'such',
        'because', 'until', 'while', 'above', 'below', 'does', 'doing', 'down',
        'having', 'might', 'must', 'need', 'still', 'under', 'upon', 'which',
        'about', 'these', 'those', 'each', 'every', 'much', 'any', 'per', 'via'
    })

    def __init__(self, master_password: str, salt: bytes = None):
        """
        Derive two independent keys from the master password:
        - data_key: for AES-256-GCM document encryption
        - search_key: for HMAC-SHA256 search token generation

        Using separate keys ensures that compromising one doesn't compromise
        the other (key separation principle).
        """
        self.salt = salt or os.urandom(16)
        self.data_key = self._derive_key(master_password, b"ciphersearch:data")
        self.search_key = self._derive_key(master_password, b"ciphersearch:search")
        self._aesgcm = AESGCM(self.data_key)

    def _derive_key(self, password: str, context: bytes) -> bytes:
        """PBKDF2-HMAC-SHA256 key derivation with contextual salt."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # 256 bits
            salt=self.salt + context,
            iterations=100_000,
        )
        return kdf.derive(password.encode('utf-8'))

    # --- Encryption / Decryption ---

    def encrypt_text(self, plaintext: str, doc_id: str) -> Tuple[str, str]:
        """
        Encrypt plaintext using AES-256-GCM.

        Args:
            plaintext: The text to encrypt
            doc_id: Used as Additional Authenticated Data (AAD) — binds ciphertext
                    to this document, preventing ciphertext swapping attacks.

        Returns:
            (ciphertext_base64, nonce_base64)
        """
        nonce = os.urandom(12)  # 96-bit nonce for GCM
        ciphertext = self._aesgcm.encrypt(
            nonce,
            plaintext.encode('utf-8'),
            doc_id.encode('utf-8')  # AAD
        )
        return (
            base64.b64encode(ciphertext).decode('ascii'),
            base64.b64encode(nonce).decode('ascii'),
        )

    def decrypt_text(self, ciphertext_b64: str, nonce_b64: str, doc_id: str) -> str:
        """
        Decrypt ciphertext using AES-256-GCM.
        Verifies integrity (GCM tag) and AAD binding automatically.
        """
        ciphertext = base64.b64decode(ciphertext_b64)
        nonce = base64.b64decode(nonce_b64)
        plaintext = self._aesgcm.decrypt(
            nonce,
            ciphertext,
            doc_id.encode('utf-8')  # AAD must match
        )
        return plaintext.decode('utf-8')

    # --- Search Token Generation ---

    def generate_token(self, keyword: str) -> str:
        """
        Generate a deterministic search token using HMAC-SHA256.

        Properties:
        - Deterministic: same keyword → same token (enables matching)
        - One-way: token → keyword is computationally infeasible
        - Keyed: without search_key, cannot generate valid tokens

        The server sees only the token, never the keyword.
        """
        normalized = keyword.lower().strip()
        token_bytes = hmac.new(
            self.search_key,
            normalized.encode('utf-8'),
            hashlib.sha256
        ).digest()
        return base64.urlsafe_b64encode(token_bytes).decode('ascii')

    def generate_ngram_tokens(self, keyword: str, n: int = 3) -> List[str]:
        """
        Generate n-gram tokens for fuzzy/substring matching.
        "diabetes" → ["$$d", "$di", "dia", "iab", "abe", "bet", "ete", "tes", "es$", "s$$"]

        Each n-gram gets its own HMAC token. Documents are matched if a threshold
        (e.g., 60%) of n-gram tokens match.
        """
        padded = f"$${keyword.lower().strip()}$$"
        ngrams = [padded[i:i+n] for i in range(len(padded) - n + 1)]
        return [self.generate_token(f"ngram:{ng}") for ng in ngrams]

    # --- Keyword Extraction ---

    def extract_keywords(self, text: str) -> List[str]:
        """Extract searchable keywords from text (remove stop words, normalize)."""
        words = re.findall(r'\b[a-zA-Z0-9]{3,}\b', text.lower())
        return sorted(set(w for w in words if w not in self.STOP_WORDS))

    # --- High-Level Operations ---

    def encrypt_document(self, doc_id: str, content: str) -> EncryptedDocument:
        """
        Full pipeline: extract keywords → generate tokens → encrypt content.
        Returns an EncryptedDocument that can be safely sent to the server.
        """
        # Encrypt content
        ct_b64, nonce_b64 = self.encrypt_text(content, doc_id)

        # Extract keywords and generate tokens
        keywords = self.extract_keywords(content)
        tokens = [self.generate_token(kw) for kw in keywords]

        return EncryptedDocument(
            doc_id=doc_id,
            encrypted_content=ct_b64,
            nonce=nonce_b64,
            tokens=tokens,
            keyword_count=len(keywords),
            timestamp=datetime.now().isoformat(),
        )

    def get_salt_b64(self) -> str:
        """Return salt as base64 (for key reconstruction)."""
        return base64.b64encode(self.salt).decode('ascii')


# ---------------------------------------------------------------------------
# Server-Side Storage & Search (UNTRUSTED)
# ---------------------------------------------------------------------------

class SecureServer:
    """
    UNTRUSTED server simulation.

    This class represents what runs on the cloud/server.
    It ONLY stores encrypted data and HMAC tokens.
    It has NO access to:
    - Master password
    - Encryption keys
    - Plaintext content
    - Original keywords

    It can ONLY:
    - Store encrypted blobs
    - Match opaque tokens
    - Return encrypted results
    """

    def __init__(self, db_path: str = "ciphersearch.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._init_db()
        self.audit_log: List[Dict] = []

    def _init_db(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS documents (
            doc_id TEXT PRIMARY KEY,
            encrypted_content TEXT NOT NULL,
            nonce TEXT NOT NULL,
            keyword_count INTEGER,
            created_at TEXT
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS search_index (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT NOT NULL,
            doc_id TEXT NOT NULL,
            FOREIGN KEY (doc_id) REFERENCES documents(doc_id) ON DELETE CASCADE
        )''')
        c.execute('CREATE INDEX IF NOT EXISTS idx_token ON search_index(token)')
        c.execute('''CREATE TABLE IF NOT EXISTS ngram_index (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT NOT NULL,
            doc_id TEXT NOT NULL,
            source_keyword_hash TEXT,
            FOREIGN KEY (doc_id) REFERENCES documents(doc_id) ON DELETE CASCADE
        )''')
        c.execute('CREATE INDEX IF NOT EXISTS idx_ngram ON ngram_index(token)')
        self.conn.commit()

    def _log(self, action: str, **details):
        entry = {
            'action': action,
            'timestamp': datetime.now().isoformat(),
            'server_note': 'Server processed opaque tokens. No plaintext accessed.',
            **details,
        }
        self.audit_log.append(entry)

    # --- Storage ---

    def store_document(self, enc_doc: EncryptedDocument):
        """Store an encrypted document and its search tokens."""
        c = self.conn.cursor()
        c.execute(
            'INSERT OR REPLACE INTO documents VALUES (?, ?, ?, ?, ?)',
            (enc_doc.doc_id, enc_doc.encrypted_content, enc_doc.nonce, 0, enc_doc.timestamp)  # keyword_count hidden to prevent info leak
        )
        c.execute('DELETE FROM search_index WHERE doc_id = ?', (enc_doc.doc_id,))
        for token in enc_doc.tokens:
            c.execute(
                'INSERT INTO search_index (token, doc_id) VALUES (?, ?)',
                (token, enc_doc.doc_id)
            )
        self.conn.commit()
        self._log('STORE_DOCUMENT', doc_id=enc_doc.doc_id, tokens_indexed=len(enc_doc.tokens))

    def store_ngram_tokens(self, doc_id: str, ngram_tokens: List[str], keyword_hash: str):
        """Store n-gram tokens for fuzzy search."""
        c = self.conn.cursor()
        for token in ngram_tokens:
            c.execute(
                'INSERT INTO ngram_index (token, doc_id, source_keyword_hash) VALUES (?, ?, ?)',
                (token, doc_id, keyword_hash)
            )
        self.conn.commit()

    # --- Search ---

    def search_token(self, token: str) -> List[Dict]:
        """Exact token matching. Returns encrypted documents."""
        c = self.conn.cursor()
        c.execute('''
            SELECT DISTINCT d.doc_id, d.encrypted_content, d.nonce
            FROM search_index si
            JOIN documents d ON si.doc_id = d.doc_id
            WHERE si.token = ?
        ''', (token,))
        results = [dict(r) for r in c.fetchall()]
        self._log('EXACT_SEARCH', token_preview=token[:16] + '...', results_found=len(results))
        return results

    def search_multi(self, tokens: List[str], operator: str = "AND") -> List[Dict]:
        """Multi-keyword search with AND/OR logic."""
        if not tokens:
            return []
        c = self.conn.cursor()
        ph = ','.join(['?'] * len(tokens))
        if operator == "AND":
            c.execute(f'''
                SELECT d.doc_id, d.encrypted_content, d.nonce
                FROM search_index si
                JOIN documents d ON si.doc_id = d.doc_id
                WHERE si.token IN ({ph})
                GROUP BY d.doc_id
                HAVING COUNT(DISTINCT si.token) = ?
            ''', (*tokens, len(tokens)))
        else:
            c.execute(f'''
                SELECT DISTINCT d.doc_id, d.encrypted_content, d.nonce
                FROM search_index si
                JOIN documents d ON si.doc_id = d.doc_id
                WHERE si.token IN ({ph})
            ''', tokens)
        results = [dict(r) for r in c.fetchall()]
        self._log(f'MULTI_SEARCH_{operator}', token_count=len(tokens), results_found=len(results))
        return results

    def search_fuzzy(self, ngram_tokens: List[str], threshold: float = 0.6) -> List[Dict]:
        """
        Fuzzy search using n-gram token matching.
        Returns documents where >= threshold fraction of n-gram tokens match.
        """
        if not ngram_tokens:
            return []
        c = self.conn.cursor()
        ph = ','.join(['?'] * len(ngram_tokens))
        c.execute(f'''
            SELECT ni.doc_id, COUNT(DISTINCT ni.token) as match_count
            FROM ngram_index ni
            WHERE ni.token IN ({ph})
            GROUP BY ni.doc_id
        ''', ngram_tokens)
        min_matches = int(len(ngram_tokens) * threshold)
        matching_doc_ids = [
            row['doc_id'] for row in c.fetchall()
            if row['match_count'] >= min_matches
        ]
        if not matching_doc_ids:
            self._log('FUZZY_SEARCH', ngram_count=len(ngram_tokens), results_found=0)
            return []
        ph2 = ','.join(['?'] * len(matching_doc_ids))
        c.execute(f'''
            SELECT doc_id, encrypted_content, nonce
            FROM documents
            WHERE doc_id IN ({ph2})
        ''', matching_doc_ids)
        results = [dict(r) for r in c.fetchall()]
        self._log('FUZZY_SEARCH', ngram_count=len(ngram_tokens), results_found=len(results))
        return results

    # --- Inspection (for Security Proof demo) ---

    def get_all_documents_raw(self) -> List[Dict]:
        """Return all stored documents (still encrypted)."""
        c = self.conn.cursor()
        c.execute('SELECT * FROM documents')
        return [dict(r) for r in c.fetchall()]

    def get_all_tokens_raw(self) -> List[Dict]:
        """Return all index entries (opaque tokens)."""
        c = self.conn.cursor()
        c.execute('SELECT token, doc_id FROM search_index LIMIT 50')
        return [dict(r) for r in c.fetchall()]

    def get_stats(self) -> Dict:
        c = self.conn.cursor()
        c.execute('SELECT COUNT(*) as n FROM documents')
        docs = c.fetchone()['n']
        c.execute('SELECT COUNT(*) as n FROM search_index')
        idx = c.fetchone()['n']
        c.execute('SELECT COUNT(DISTINCT token) as n FROM search_index')
        uniq = c.fetchone()['n']
        return {
            'documents': docs,
            'index_entries': idx,
            'unique_tokens': uniq,
            'audit_events': len(self.audit_log),
        }

    def delete_document(self, doc_id: str):
        c = self.conn.cursor()
        c.execute('DELETE FROM search_index WHERE doc_id = ?', (doc_id,))
        c.execute('DELETE FROM ngram_index WHERE doc_id = ?', (doc_id,))
        c.execute('DELETE FROM documents WHERE doc_id = ?', (doc_id,))
        self.conn.commit()
        self._log('DELETE', doc_id=doc_id)

    def clear_all(self):
        c = self.conn.cursor()
        c.execute('DELETE FROM search_index')
        c.execute('DELETE FROM ngram_index')
        c.execute('DELETE FROM documents')
        self.conn.commit()
        self.audit_log.clear()


# ---------------------------------------------------------------------------
# Standalone demo (for testing without Streamlit)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 65)
    print(" CipherSearch — Standalone Demo")
    print("=" * 65)

    engine = CipherSearchEngine("hackathon_demo_2024")
    server = SecureServer(":memory:")

    docs = {
        "P001": "Patient John Smith diagnosed with Type 2 Diabetes and Hypertension. "
                "Prescribed Metformin 500mg and Lisinopril 10mg.",
        "P002": "Patient Jane Doe reports chronic migraine and anxiety. "
                "Prescribed Sumatriptan and Sertraline.",
        "P003": "Patient Bob Chen has Coronary Artery Disease and Diabetes. "
                "On Aspirin, Atorvastatin, and Metformin.",
    }

    print("\n[UPLOAD] Encrypting and storing documents...\n")
    for doc_id, content in docs.items():
        enc = engine.encrypt_document(doc_id, content)
        server.store_document(enc)
        print(f"  [OK] {doc_id}: {enc.keyword_count} keywords -> "
              f"{len(enc.tokens)} tokens | "
              f"ciphertext: {enc.encrypted_content[:40]}...")

    print("\n[SEARCH] Searching for 'diabetes'...\n")
    token = engine.generate_token("diabetes")
    print(f"  Token: {token[:40]}...")
    results = server.search_token(token)
    print(f"  Found {len(results)} encrypted result(s)")
    for r in results:
        plain = engine.decrypt_text(r['encrypted_content'], r['nonce'], r['doc_id'])
        print(f"  [DOC] {r['doc_id']}: {plain[:80]}...")

    print("\n[SEARCH] Multi-keyword AND search: 'diabetes' + 'metformin'...\n")
    tokens = [engine.generate_token("diabetes"), engine.generate_token("metformin")]
    results = server.search_multi(tokens, "AND")
    print(f"  Found {len(results)} result(s)")
    for r in results:
        plain = engine.decrypt_text(r['encrypted_content'], r['nonce'], r['doc_id'])
        print(f"  [DOC] {r['doc_id']}: {plain[:80]}...")

    print("\n[SECURITY] Server's view (what an attacker sees):")
    for d in server.get_all_documents_raw():
        print(f"  {d['doc_id']}: {d['encrypted_content'][:50]}... [UNREADABLE]")

    print("\n[DONE] Demo complete. Server never saw any plaintext.")