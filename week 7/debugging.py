"""CP1401 - Practical 7 - Debugging.
The "demo" problem shows how the answers should be written.
Follow the example and template to answer the questions (find and fix problems) below.
"""


# Questions start here:

def main_1():
    """Determine the parity of a user's number."""
    number = int(input("Enter number: "))
    parity = calculate_parity(number)
    print(parity)


def calculate_parity(number):
    """Calculate the parity (0 or 1) of number passed in."""
    return number % 2


# Problem(s) for program 1:
# ? <function calculate_parity at 0x0000023F71CED1F0>

# Fixed code for program 1:
# parity = calculate_parity(number)

def main_2():
    """Print numbers from 0 up to the user's input multiplied by 2."""
    # E.g., if input is 12, should print 0 2 4 6 8 10 12 14 16 18 20 22 24
    numnums = int(input("How many: "))
    for i in range(numnums):
        print(i * 2, end=" ")


# Problem(s) for program 2:
# numnums ={str}12
# TypeError: 'int' object is not iterable

# Fixed code for program 2:
# numnums = int(input("How many: "))
# for i in range(numnums):


def main_3():
    """Determine the area of a rectangle."""
    length, width = 12, 10
    area = calculate_area(length, width)
    print(f"The area is {area}")


def calculate_area(long, wide):
    """Calculate the area of a rectangle from its dimensions."""
    result = long * wide
    return result


# Problem(s) for program 3:
# The result is not return to the main function

# Fixed code for program 3:
# return result

def main_4():
    """Show how old a person will be in the future."""
    increment = 10
    age = int(input("Age: "))
    new_age = calculute_age(age, increment)
    while age < 0 or age > 120:
        print("Invalid age")
        age = int(input("Age: "))
    print(f"In {increment} years, you will be {new_age} years old!")


def calculute_age(age, increment):
    result = age + increment
    return result
# Problem(s) for program 4:
# 1. CONSTANT number should be ALL_CAP
# 2. Out of range should be use "or"
# 3. the future age result should be calculated

# Fixed code for program 4:
# 1.INCREMENT = 10
# 2.while age < 0 or age > 120:
# 3.print(f"In {INCREMENT} years, you will be {new_age} years old!")
#
# def calculute_age(age, INCREMENT):
#     result = age + INCREMENT
#     return result
# demo()
# main_1()
# main_2()  # Note: these are not good names; just something to reduce the amount of copying we need to do
# main_3()
# main_4()
