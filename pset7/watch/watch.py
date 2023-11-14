import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(r"iframe .*src=\".*youtube\.com/embed/([\w]+)", s):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return "None"


if __name__ == "__main__":
    main()
