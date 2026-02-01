# 🔐 CAESARTOOL

CAESARTOOL is a **Kali Linux–style cryptography CLI tool** written in Python.  
It provides an interactive terminal-based interface for performing **classical encryption** and **modern cryptographic hashing**, similar to tools used in cybersecurity environments.

This project is suitable for **educational use, internships, and cybersecurity practice**.

---

## 📌 About the Tool

CAESARTOOL allows users to perform cryptographic operations using a simple menu-driven interface.

### 🔁 Caesar Cipher
- Encrypt text using a shift value
- Decrypt encrypted text using the same shift
- Reversible classical encryption technique

### 🔒 Hash Generator
- MD5
- SHA1
- SHA256
- One-way hashing (decryption is not possible by design)

The tool follows **secure design principles** by allowing decryption only where mathematically possible.

---

## 🚀 Features

- Kali Linux–style interactive CLI
- Random ASCII banner on every run
- Caesar Cipher encryption & decryption
- Secure hash generation (MD5, SHA1, SHA256)
- Built-in help section
- Clean and professional output
- Proper Python packaging using `pipx`

---
## Steps for Install in Linux

```bash
git clone https://github.com/cyberrockyroom/caesartool.git
cd caesartool

```
## 🛠️ Requirements

Before installing the tool, make sure your system has:

- **Python 3.10 or higher**
- **Git**
- **pipx** (recommended)

Check Python version:
```bash
python3 --version
sudo apt update
sudo apt install pipx -y
pipx ensurepath


