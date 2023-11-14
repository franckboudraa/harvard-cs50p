months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        user_input = input("Date: ").strip()

        if "," not in user_input and "/" not in user_input:
            raise ValueError

        month, day, year = user_input.replace(", ", "/").replace(",", "/").replace(" ", "/").split("/")

        if month.isalpha():
            month_index = months.index(month)

            if user_input[month_index + 1] != " ":
                raise ValueError
            
            month = months.index(month) + 1

        if int(month) > 12 or int(day) > 31:
            raise ValueError

        print(f"{year}-{int(month):02}-{int(day):02}")

        break
    except (EOFError, ValueError):
        pass