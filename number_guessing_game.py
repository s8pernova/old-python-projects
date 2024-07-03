import random
import time

min_numb = 1
max_numb = 5

def invalid_input():
    print("D00d..... that's not a valid input. Try again.")
    time.sleep(3)
    print()

while True:
    chosen_numb = random.randint(min_numb, max_numb)

    user_input = int(input(f"I'm guessing of a number between {min_numb} and {max_numb}. Try and guess it!!: "))

    if user_input == chosen_numb:
        break
    elif user_input < min_numb or user_input > max_numb:
        invalid_input()
    elif user_input != int(chosen_numb):
        print(f"WRONG! You fail. I guessed {chosen_numb}. Try again until you guess CORRECTLY.")
        time.sleep(3)
        print()
    else:
        invalid_input()

print("Oh. I guess you won. Congrats...")