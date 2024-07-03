import random
import time

user_input = str(input("Welcome to the dice game! Would you like to roll a dice? [Y/N]: ").lower())

if user_input == "n":
    print("\nThen get out of here already.")
    exit()
elif user_input == "y":
    while True:
        print("\nRolling the dice...")
        time.sleep(3)
        print(f"The dice landed on {random.randint(1,6)}")
        user_input = str(input("\nRoll again? [Y/N]: ")).lower()
        if user_input == "n":
            print("\nThen get out of here already.")
            break
        elif user_input == "y":
            continue