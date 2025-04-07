# we are going to hash a password using bycrypt library
# bcrypt is a password hashing function designed by Niels Provos and David Mazières, based on the Blowfish cipher
# bcrypt is a password hashing function designed for secure password storage
# install bcrypt library using pip
# pip install bcrypt

import bcrypt

password = "password123" # Password to hash

# Generate a salt for hashing the password
salt = bcrypt.gensalt() 
# salt is a random value added to the password before hashing it makes the hash unique and secure
# bcrypt.gensalt() function generates a random salt for hashing a password

# Hashing the password
hashed = bcrypt.hashpw(password.encode(), salt) # Hash password and salt

# hashpw() function returns a hashed version of the password
# password.encode() function converts the password string to bytes

# Print the hashed password
print("Original password: ", password)
print(f"Hashed password: {hashed.decode('utf-8')}") # Decode bytes to string

# decode() function converts the bytes to string
# utf-8 is the encoding format used to convert the bytes to string  (utf-8 is the default encoding format)


