# CipherSearch — Secure String Matching on Encrypted Data

**Hack-A-League 4.0 | Theme: Ignite The Future | Sector: Security and Privacy**

> Design and develop a secure system that enables string matching on encrypted data while preserving data confidentiality and privacy.

## Problem

Organizations must encrypt sensitive data for compliance (HIPAA, GDPR). But encryption makes data unsearchable — you either sacrifice privacy or functionality.

## Solution

CipherSearch enables **searching encrypted data without ever decrypting it on the server**. The server matches cryptographic tokens blindly — it finds your results without learning anything about your data or your queries.

## Architecture

```
┌────────────────── CLIENT (Trusted) ──────────────────┐
│  Master Password → PBKDF2 → Data Key + Search Key    │
│  AES-256-GCM encrypt/decrypt | HMAC-SHA256 tokens    │
└──────────────────────┬───────────────────────────────┘
                       │ Encrypted blobs + opaque tokens only
                       ▼
┌────────────────── SERVER (Untrusted) ────────────────┐
│  SQLite: encrypted_content, search_index (tokens)    │
│  Matches tokens blindly • NO keys • NO plaintext     │
└──────────────────────────────────────────────────────┘
```

**Trust boundary:** Keys and plaintext NEVER cross into the server.

## Cryptographic Building Blocks

| Component | Purpose |
|-----------|---------|
| **AES-256-GCM** | Authenticated encryption (confidentiality + integrity) |
| **HMAC-SHA256** | Deterministic search tokens — same keyword → same token |
| **PBKDF2** | 100,000 iterations for password-to-key derivation |

## Features

- **Exact keyword search** — Single-term queries
- **Multi-keyword AND/OR** — Comma-separated queries
- **Fuzzy / typo-tolerant search** — N-gram matching (e.g., "diabtes" → "diabetes")
- **Security Proof page** — View raw server data (encrypted blobs, opaque tokens)
- **Performance benchmark** — Measure encrypt/token/search throughput

## Quick Start

```bash
# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Standalone Demo (No Streamlit)

```bash
python crypto_engine.py
```

Runs a terminal demo: encrypt sample medical records, search for "diabetes", multi-keyword search.

## Project Structure

```
ciphersearch/
├── crypto_engine.py    # CipherSearchEngine + SecureServer
├── app.py              # Streamlit UI (6 pages)
├── requirements.txt
├── README.md
├── screenshots/        # Demo screenshots for submission
└── .gitignore
```

## Use Cases

- **Healthcare** — Encrypted patient records searchable by doctors
- **Finance** — Compliance search on encrypted transaction logs
- **Legal** — Privilege-protected document discovery
- **Education** — Secure student records with searchable access

## Team

Built for Hack-A-League 4.0 by Global Academy of Technology.

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/c9dbfa5b-6e09-4e1f-8a11-ce8efaa5e97f" />



