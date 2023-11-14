due = 50

while due > 0:
    user_coin = int(input("Insert Coin: "))

    if user_coin in [5, 10, 25]:
        due -= int(user_coin)

    if due > 0:
        print(f"Amount Due: {due}")
    else:
        break

print(f"Change Owed: {abs(due)}")