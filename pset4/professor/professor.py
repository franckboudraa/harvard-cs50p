import random


def main():
    correct_answers = 0
    level = get_level()
    ops = generate_ops(10, level)

    for op in ops:
        while op["tries"] != 3:
            print(f"{op["num_1"]} + {op["num_2"]} =", end=" ")
            user_input = int(input())

            if op["num_1"] + op["num_2"] != user_input:
                op["tries"] += 1

                print("EEE")

                if(op["tries"] == 3):
                    print(f"{op["num_1"]} + {op["num_2"]} = {op["num_1"] + op["num_2"]}", end=" ")
            else:
                correct_answers += 1
                break

    print(f"Score: {correct_answers}")

def get_level():
    while True:
        try:
            user_input = int(input("Level: "))

            if 0 < user_input < 4:
                pass
            else:
                raise ValueError
        except:
            continue

        return user_input


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


def generate_op(level):
    return { "num_1": generate_integer(level), "num_2": generate_integer(level), "tries": 0 }


def generate_ops(count, level):
    ops = []

    while len(ops) < count:
        ops.append(generate_op(level))

    return ops


if __name__ == "__main__":
    main()
