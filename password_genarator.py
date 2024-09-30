# import random
# input=int(input("enter how many nubmers you want to generate password:"))
# alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# digits='0123456789'
# symbols='!@#$%^&*()_+}{:"'
# all_add=alphabets+digits+symbols
#
# generate=random.sample(all_add,input)
# password=''.join(generate)
# print(generate)
# print(password)

import random

def generate_password(num_chars):
    if 4 < num_chars < 9:
        seq = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        symbols='!@#$%^&*()_+}|'
        digits='1234567890'
        gen=seq+symbols+digits
        pwd=random.sample(gen,num_chars)
        return ''.join(pwd)
    else:
        return 'You have to select a correct option (between 5 and 8 characters).'

try:
    user_input = int(input("Enter the number of characters you want to generate (5-8): "))
    password = generate_password(user_input)
    print(password)
except ValueError:
    print("Please enter a valid number.")
