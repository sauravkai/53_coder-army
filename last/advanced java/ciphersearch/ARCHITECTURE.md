# CipherSearch Architecture

## Security Model

### Trust Boundary

- **Client zone:** Holds master password, derives keys locally, encrypts/decrypts, generates search tokens.
- **Server zone:** Stores encrypted blobs and opaque HMAC tokens. Performs token matching only.
- **Invariant:** Keys and plaintext NEVER cross into the server. `SecureServer` has no access to `CipherSearchEngine` keys.

### Key Separation

Two independent 256-bit keys are derived from the master password via PBKDF2:

1. **data_key** — Used for AES-256-GCM document encryption
2. **search_key** — Used for HMAC-SHA256 search token generation

Context strings (`ciphersearch:data`, `ciphersearch:search`) ensure key domain separation.

## Data Flow

### Document Upload

1. Client extracts keywords (stop words removed, min 3 chars)
2. Client encrypts content with AES-256-GCM (doc_id as AAD)
3. Client generates HMAC tokens for each keyword
4. Client sends `{doc_id, encrypted_content, nonce, tokens}` to server
5. Server stores in SQLite — no plaintext, no keys

### Search (Exact)

1. Client normalizes query → generates HMAC token with search_key
2. Client sends token to server
3. Server matches token in `search_index` → returns encrypted blobs
4. Client decrypts locally

### Search (Fuzzy)

1. Client generates n-gram tokens (e.g., "diabetes" → 10 trigram tokens)
2. Server matches documents with ≥ threshold fraction of n-grams
3. Returns encrypted results; client decrypts

## Database Schema

```sql
-- Encrypted documents (no plaintext)
documents(doc_id, encrypted_content, nonce, keyword_count, created_at)

-- Exact keyword search index (opaque tokens)
search_index(token, doc_id)
-- Index on token for O(1) lookup

-- Fuzzy search (n-gram tokens)
ngram_index(token, doc_id, source_keyword_hash)
```

## Threat Model

- **Server compromise:** Attacker sees encrypted blobs and tokens. Cannot decrypt without key; tokens are one-way.
- **Passive eavesdropper:** All traffic is encrypted; tokens reveal no keyword information without search_key.
- **Ciphertext swapping:** AAD (doc_id) binds ciphertext to document; tampering detected by GCM.
