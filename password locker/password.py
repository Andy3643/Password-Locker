import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
while True:
    password_length = int (input("How many Characters do you want:"))
    created_password = ""
    for x in range (0, password_length):
        password_char = random.choice(chars)
        created_password = created_password + password_char
    print("Your password is :",created_password)