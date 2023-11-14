number1, sign, number2 = input("Expression: ").strip().lower().split(" ")

match sign:
    case "+":
        print(float(number1) + float(number2))
    case "-":
        print(float(number1) - float(number2))
    case "*":
        print(float(number1) * float(number2))
    case "/":
        print(float(number1) / float(number2))