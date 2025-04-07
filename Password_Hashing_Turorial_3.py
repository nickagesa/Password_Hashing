# This is a simple password hashing tutorial using bcrypt in Python.
# In this tutorial, we will learn how to verify the password using bcrypt library in Python.

import bcrypt

password = "password123" # Password to hash

# generate a salt and hash the password
salt = bcrypt.gensalt() # Generate a salt

# bcrypt.gensalt() function generates a random salt for hashing a password

# Hashing the password
hashed = bcrypt.hashpw(password.encode(), salt) # Hash password and salt

# hashpw() function returns a hashed version of the password
# password is the variable that contains the password
# .encode() function converts the password string to bytes
# salt is the variable that contains the salt

# Print the hashed password
print(f"Hashed password: {hashed.decode('utf-8')}") # Decode bytes to string

# decode() function converts the bytes to string
# utf-8 is the encoding format used to convert the bytes to string  (utf-8 is the default encoding format)

# Verify the password
if bcrypt.checkpw(password.encode(), hashed): # Check if password is correct
    print("Password is correct") # Print if password is correct
else:
    print("Password is incorrect") # Print if password is incorrect

# checkpw() function checks if the password is correct
# password.encode() function converts the password string to bytes
# hashed is the hashed password


