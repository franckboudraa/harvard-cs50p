def main():
    userInput = input("What time is it? ").strip().lower()

    time = convert(userInput)

    if 7 <= time <= 8.0:
        print("breakfast time")
    elif 12 <= time <= 13.0:
        print("lunch time")
    elif 18 <= time <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")

    return float(hours) + float(int(minutes) / 60)

if __name__ == "__main__":
    main()
