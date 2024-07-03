import time

age = 1

def wait():
    time.sleep(0.5)

print("Happy birthday to you!")
wait()
print("Happy birthday to you!")
wait()
print("Happy birthday, happy birthday.")
wait()
print("Happy birthday to you!")
wait()
print()

while True:
    print(f"Are you {age}?")
    age += 1
    time.sleep(0.0001)
