"""
# Task 1
print("Hello, World!")

# Task 2
name = input("What is your name?: ")
print(f"\nHello, {name.title}. Nice to meet you. Probably. I wouldn't know. I'm just a robot.")

# Task 3
a = int(input("Pick a number: "))
b = int(input("\nNow pick another number: "))
print(f"\nThose two numbers combined are equal to {a+b}")

# Task 4
user_num = int(input("Give me a prime number (numbers that can only be divided by itself): "))

# variable to test if the number can only be divided by itself
prime_num = 

for x in range
"""

# Task 6
def sum_even_numbers(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum

my_input = [13, 421, 58, 90, 37, 85, 67, 44]
print(sum_even_numbers(my_input))