import re

def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if matches := re.search(r"^(1[0-9]|[0-9]):?([0-5]?[0-9]?) (AM|PM) to (1[0-9]|[0-9]):?([0-5]?[0-9]?) (AM|PM)$", s):
        from_h, from_m, from_type, to_h, to_m, to_type = matches.groups()

        from_h = convert_hour_in_24_fmt(from_h, from_type)
        to_h = convert_hour_in_24_fmt(to_h, to_type)

        from_m = correct_minute(from_m)
        to_m = correct_minute(to_m)

        return f"{from_h:02d}:{from_m:02d} to {to_h:02d}:{to_m:02d}"
    else:
        raise ValueError


def convert_hour_in_24_fmt(hour, type):
    if type == "AM":
        if hour == "12" or hour == "":
            return 0
        else:
            return int(hour)
    else:
        if hour == "12":
            return int(hour)
        else:
            return 12 + int(hour)

def correct_minute(minute):
    if minute == "":
        return 0
    else:
        return int(minute)

if __name__ == "__main__":
    main()
