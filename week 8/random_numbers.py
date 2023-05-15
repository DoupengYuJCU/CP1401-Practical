import random
from random import choice


def main():
    quantity_of_number = get_numbers("How many random numbers: ", 1, 10)
    maximum_number = get_numbers("Maximum number: ", 1, 100)
    random_numbers = []
    if random_numbers != "":
        for i in range(quantity_of_number):
            random_numbers.append(random.randint(0, maximum_number))
        print(random_numbers)
        minimum_number = min(random_numbers)
        print(f"The minimum is {minimum_number}")
        maximum_number = max(random_numbers)
        print(f"The maximum is {maximum_number}")
        print(f"A randomly chosen number is {random.choice(random_numbers)}.")
        random_numbers.sort()
        print(f"The numbers sorted are {random_numbers}")
        random_numbers.reverse()
        print(f"The numbers reversed are {random_numbers}")


def get_numbers(prompt, low, high):
    number = int(input(prompt))
    while number < low or number > high:
        print("Invalid number")
        number = int(input(prompt))
    return number


main()