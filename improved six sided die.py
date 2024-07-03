import random
import time

def invalid_option():
    print("\nThat's not a valid option. How could you fail at something so simple? Just go home... I can't bear to look at you anymore......")
    exit()

counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
counter_6 = 0

user_input = str(input("Welcome to the dice game! Would you like to roll a dice 600 times? [Y/N]: ").lower())

if user_input == "n":
    print("\nThen get out of here already.")
    exit()
elif user_input == "y":
    print("\nRolling the dice...")
    time.sleep(3)
    for _ in range(0, 600):
        randomness = random.randint(1,6)
        if randomness == 1:
            counter_1 += 1
        elif randomness == 2:
            counter_2 += 1
        elif randomness == 3:
            counter_3 += 1
        elif randomness == 4:
            counter_4 += 1
        elif randomness == 5:
            counter_5 += 1
        elif randomness == 6:
            counter_6 += 1
else:
    invalid_option()

print(f"\nThe dice landed on {counter_1} 1's ({round((counter_1/600)*100, 2)}%), {counter_2} 2's ({round((counter_2/600)*100, 2)}%), {counter_3} 3's ({round((counter_3/600)*100, 2)}%), {counter_4} 4's ({round((counter_4/600)*100, 2)}%), {counter_5} 5's ({round((counter_5/600)*100, 2)}%), and {counter_6} 6's ({round((counter_6/600)*100, 2)}%).")
print("\nThanks for playing! Goodbye.")