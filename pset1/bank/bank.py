userInput = input("Greeting: ").strip().lower()

if "hello" in userInput:
    print("$0")
elif userInput.startswith("h"):
    print("$20")
else:
    print("$100")