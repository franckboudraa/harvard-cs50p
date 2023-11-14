from sys import argv, exit
from random import choice
from pyfiglet import Figlet

f = Figlet()
font = choice(f.getFonts())

try:
    if len(argv) == 2 or len(argv) == 3 and argv[1] != '-f' and argv[1] != '--font':
        exit("Invalid usage")
    elif argv[1] == '-f' or argv[1] == '--font' and argv[2] != None:
        font = argv[2]
except IndexError:
    pass

f.setFont(font=font)

user_input = input("Input: ")

print("Output: ")
print(f.renderText(user_input))
