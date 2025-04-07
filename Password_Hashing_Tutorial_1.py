# This script demonstrates how to hash a password using SHA-256.
# SHA-256 is a cryptographic hash function that produces a 256-bit hash value.
# It is part of the SHA-2 family of hash functions, designed by the NSA.
# hashlib is a built-in Python library that provides a common interface to many secure hash and message digest algorithms, including SHA1, SHA224, SHA256, SHA384, SHA512, MD5, etc.

import hashlib # Import the hashlib library for hashing

password = "password123"  # Password to hash

# Encode the password to bytes, then hash it
hashed = hashlib.sha256(password.encode()).hexdigest() # Hash the password using SHA-256 and convert it to a hexadecimal string
# sha256() function takes a string as input and returns a hash object
# encode() function converts the password string to bytes
# hexdigest() function returns the hash value as a hexadecimal string

print(f"Your hashed password is: {hashed}") # Print the hashed password

'''
❌ Important Note:❌
hashlib is good for hashing, but it’s not the most secure option for storing passwords.
This is because it’s fast, and fast algorithms are vulnerable to brute-force attacks.
For real-world applications, always use something like bcrypt, argon2, or pbkdf2_hmac for password hashing since they include salting and are intentionally slow.'''



