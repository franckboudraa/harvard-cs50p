from random import randint
from sys import exit

num_to_find = None

while True:
    if num_to_find == None:
        try:
            user_input = input("Level: ")

            if user_input.isnumeric() == False:
                raise ValueError

            user_input = int(user_input)
        except:
            continue

        if user_input < 1:
            continue

        num_to_find = randint(1, user_input)

    try:
        user_input = input("Guess: ")

        if user_input.isnumeric() == False:
            raise ValueError

        user_input = int(user_input)
    except:
        continue

    if user_input < num_to_find:
        print("Too small!")
        continue
    elif user_input > num_to_find:
        print("Too large!")
        continue
    else:
        exit("Just right!")
