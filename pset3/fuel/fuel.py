while True:
    try:
        user_input = input("Fraction: ")
        splitted_input = user_input.split("/")

        f = int(splitted_input[0])
        s = int(splitted_input[1])

        if f > s:
            raise ValueError

        fuel = round((int(f) / int(s)) * 100)

        if fuel >= 99:
            res = "F"
        elif fuel <= 1:
            res = "E"
        elif fuel > 100:
            pass
        else:
            res = f"{fuel}%"

        print(res)
        break
    except (ValueError, ZeroDivisionError):
        pass