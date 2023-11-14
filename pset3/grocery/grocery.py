groceries = {}

while True:
    try:
        user_input = input().strip().upper()

        try:
            groceries[user_input] +=1

        except KeyError:
            groceries[user_input] = 1

    except EOFError:
        break

for grocery in dict(sorted(groceries.items())):
    print(f"{groceries[grocery]} {grocery}")