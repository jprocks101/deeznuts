import os
import random
import string


def credits():
    os.system('cls')
    print("Nitro gen by jp")
    input('Press enter to continue ...')
    generator()

def generator():
    os.system('cls')
    numbers = int(input('How many nitro do you want to generate : '))
    for i in range(numbers):
        code = "https://discord.gift/" + "".join(random.choices(string.ascii_letters + string.digits, k=16))
        print('[GENERATED]' + " " + code)
        nitroList = open('nitro.txt', 'a')
        nitroList.write(code + "\n")

if __name__ == '__main__':
    credits()