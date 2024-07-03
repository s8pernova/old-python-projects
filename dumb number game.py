import time

def game_over():
    print()
    print("Oh... you failed...,., You chose a number outside of the range..........,,,.. Just,,.,. get out..,.,.")
    time.sleep(5)
    exit()
    
def game_over_again():
    print()
    print("That's the same number d00d. Retry.")
    time.sleep(5)
    exit()

x = int(input("Say a number 1-10: "))
if x < 1:
    game_over()
if x > 10:
    game_over()

y = int(input("Now say another number 1-10: "))
if y < 1:
    game_over()
if y > 10:
    game_over()

if x > y:
    print(f"\n{x} is larger.")
elif y > x:
    print(f"\n{y} is larger.")
else:
    game_over_again()