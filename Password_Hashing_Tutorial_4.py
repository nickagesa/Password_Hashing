# we are going to add key derivation function to the password hashing
# Key derivation function is a function that derives one or more secret keys from a secret value such as a password or passphrase using a pseudo-random function
# Key derivation functions are used to securely hash passwords and protect them from brute force attacks

import bcrypt

password = "password123" # Password to hash

salt = bcrypt.gensalt() # Generate a random salt

# Using KDF (Key Derivation Function) to hash the password
key = bcrypt.kdf(password=password.encode(), salt=salt, desired_key_bytes=32, rounds=200)

# kdf() is used to hash the password
# password.encode() function converts the password string to bytes
# salt is variable that contains the salt
# desired_key_bytes is the desired length of the key
# rounds is the number of iterations to perform on the password and salt before returning the key  (default is 12)

print(f"Key: {key}") # Print the hashed password

# Verify the password

if bcrypt.kdf(password="password123".encode(), salt=salt, desired_key_bytes=32, rounds=200) == key:
    print("Password is correct")
else:
    print("Password is incorrect")




