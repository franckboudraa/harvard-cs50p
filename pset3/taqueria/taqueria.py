menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    client = {
        "bill": 0,
        "choices": []
    }

    while True:
        try:
            choose_item(client, ask_client())
        except EOFError:
            break

def ask_client():
    return input("Item: ").title()

def choose_item(client, choice):
    if choice in menu:
        client['choices'].append(choice)
        client['bill'] += menu[choice]

        print(f"Total: ${client['bill']:.2f}")

main()