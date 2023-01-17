import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()"*3)

def generate_password():
    pass_len = int(input("Password Length? - "))
    random.shuffle(characters)
    password = characters[:pass_len]
    return ''.join(password)

while True:
    if input("Do you want to generate Password?(Y/N)") in ('Y', 'y'):
        print(generate_password())
    else:
        print("Program Terminated")
        quit()
