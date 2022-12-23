import random
passlen = int(input("Enter the length of the password"))
a = "qwertyuiopasdfghjklzxcvbnm1234567890@#$&-+()/*:;!?~√π÷×¶∆£¢€¥^°={}\%©®™✓[]"
b = "".join(random.sample(a,passlen))
print(b)