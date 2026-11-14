# 🔒 Secure 7-Char Cipher CLI

A lightweight, robust command-line interface (CLI) tool written in Python that provides end-to-end symmetric encryption for messages using a short, highly-entropy 7-character secret code (mixing uppercase, lowercase, numbers, and special symbols).

---

## 🚀 Features

* **End-to-End Security:** Uses industry-standard **AES encryption** (via Fernet) combined with **PBKDF2-HMAC-SHA256** key derivation (100,000 iterations) to turn a short code into a cryptographic key.
* **High Entropy 7-Char Keys:** Automatically generates a random 7-character code comprising:
  * Uppercase letters (`A-Z`)
  * Lowercase letters (`a-z`)
  * Digits (`0-9`)
  * Special symbols (`@`, `#`, `$`, `+`, etc.)
* **Zero-Knowledge / Serverless Transport:** The cipher text and cryptographic salt are safely packaged together, meaning you can share the encrypted blob over any insecure channel (chat apps, email, pastebins) while sharing the 7-character key through a separate, secure channel.
* **Fail-Safe Decryption:** Any modification to the cipher text or an incorrect 7-character code will immediately fail to decrypt, preventing tampering.

---

## 🛠️ Prerequisites & Installation

Make sure you have **Python 3.8+** installed on your system.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/secure-7char-cipher.git](https://github.com/YOUR_USERNAME/secure-7char-cipher.git)
   cd secure-7char-cipher
