def show_help():
    print("""
================ CAESARTOOL HELP =================

[1] Caesar Cipher
    - Encrypt and decrypt text using shift value
    - Example:
      Encrypt : caesartool → Caesar → Encrypt
      Decrypt : caesartool → Caesar → Decrypt

[2] Hash Generator
    - Generate one-way hash values
    - Supported algorithms:
      * MD5
      * SHA1
      * SHA256
    - Hashes cannot be decrypted

Notes:
- Caesar cipher is reversible
- Hashing is irreversible
- This tool follows Kali Linux style interaction

Author : Kiran Patel
==================================================
""")
