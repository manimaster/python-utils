"""
Password Generator

This script generates a random password that the user can use for their applications.
"""

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter desired password length: "))
print("Generated Password:", generate_password(length))
