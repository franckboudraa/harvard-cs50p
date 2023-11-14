def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # “All vanity plates must start with at least two letters.”

    # “… vanity plates may contain a maximum of 6 characters (letters or numbers)
    # and a minimum of 2 characters.”
    if len(s) < 2 or len(s) > 6:
        return False

    # “Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not
    # be acceptable. The first number used cannot be a ‘0’.”

    number_count = 0

    for i in range(0, len(s)):
        if s[i].isnumeric() == False:
            continue
        elif number_count == 0 and s[i] == "0":
            return False
        elif i == len(s) - 1 or (s[i + 1]).isnumeric():
            number_count += 1
            continue
        else:
            return False

    # “No periods, spaces, or punctuation marks are allowed.”
    if s.isalnum() == False:
        return False

    return True

main()