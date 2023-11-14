fruit = input("Item: ").lower()

calories = 0

match fruit:
    case "apple":
        calories = 130
    case "avocado" | "cantaloupe" | "honeydew melon" | "pineapple" | "strawberries" | "tangerine":
        calories = 50
    case "banana":
        calories = 110
    case "grapefruit" | "nectarine" | "peach":
        calories = 60
    case "grapes" | "kiwifruit":
        calories = 90
    case "lemon":
        calories = 15
    case "lime":
        calories = 20
    case "orange" | "watermelon":
        calories = 80
    case "pear" | "sweet cherries":
        calories = 100
    case "plums":
        calories = 70

if calories != 0:
    print(f"Calories: {calories}")
else:
    print("")