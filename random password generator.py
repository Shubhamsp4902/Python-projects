# mini project for random password generator in python

import random
passlen = int(input("Enter the length of password you want to generate"))
char = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890@#$&£¢€¥π"
password = "".join(random.sample(char, passlen))
print(password)