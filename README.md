# Password Hashing 101 🛡️
Welcome to the Password Hashing Tutorial Series!  
This repository is designed to help you understand the importance of secure password storage and guide you step-by-step from the basics to advanced hashing techniques.

## Why Is Password Hashing Important?

Storing passwords as plain text is a huge security risk.  
If your database is ever compromised, all user accounts become exposed instantly.  
This project walks you through the evolution of password handling — from plain text storage to modern, secure methods like bcrypt and key derivation functions (KDF).

Make sure to start by reading the included PDF for a solid foundation:

<h3>📖 <a href="https://github.com/nickagesa/Password_Hashing/blob/main/Understanding_Password_Hashing.pdf">Understanding_Password_Hashing.pdf</a></h3>

This document explains:
- Why storing plain text passwords is dangerous
- The concept of hashing
- Salting passwords for extra protection
- Bcrypt and its advantages
- Key Derivation Functions (KDF)
- An introduction to OAuth 2.0 for delegated authorization

## 🚀 Tutorials Breakdown

Follow the tutorials in order to build your knowledge progressively.
password_hashing_tutorial_1.py to password_hashing_tutorial_4.py

## ✅ Final Recommendation

For real-world applications, prefer:
- ✅ **bcrypt**  
- ✅ **PBKDF2** (or libraries using it, like `passlib`)

Avoid using `hashlib` alone for password storage — it’s great for other uses but not secure enough for protecting passwords.

---

Happy learning and stay secure! 🔒✨
