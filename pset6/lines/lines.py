from sys import argv, exit

lines_count = 0

if len(argv) != 2:
    exit("Too few command-line arguments")

if argv[1].endswith(".py") == False:
    exit("Not a Python file")

try:
    with open(argv[1]) as file:
        for line in file:
            if line.lstrip().startswith("#") or line.lstrip().isspace() or line.lstrip() == '':
                pass
            else:
                lines_count += 1
    print(lines_count)

except FileNotFoundError:
    exit("File does not exist")
