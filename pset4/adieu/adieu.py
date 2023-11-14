names = []

while True:
    try:
        user_input = input("Name: ")

        names.append(user_input)
    except EOFError:
        break

print("")
print("Adieu, adieu, to ", end="")

for name in names:
    if len(names) == 2 and names.index(name) == len(names) - 2:
        print(name, end=" and ")
    elif names.index(name) == len(names) - 2:
        print(name, end=", and ")
    elif names.index(name) == len(names) - 1:
        print(name)
    else:
        print(name, end=", ")
