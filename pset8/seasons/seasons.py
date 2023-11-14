import sys
import inflect
from datetime import date

p = inflect.engine()

def main() -> None:
    user_input = input("Date of Birth: ")

    print(convert(user_input))


def convert(input: str) -> str:
    diff = get_diff_minutes(get_date_today_midnight(), get_date(input))

    return prettier_delta(format_delta(diff))


def get_date(input: str) -> date:
    try:
        return date.fromisoformat(input)
    except:
        sys.exit("Invalid date")


def get_date_today_midnight() -> date:
    return date.today()


def get_diff_minutes(date1: date, date2: date) -> int:
    timedelta = date2 - date1

    return abs(int(timedelta.total_seconds() / 60))


def format_delta(delta: int) -> str:
    return p.number_to_words(delta)


def prettier_delta(formatted_delta: str) -> str:
    return f"{formatted_delta} minutes".replace(" and ", " ").capitalize()


if __name__ == "__main__":
    main()
