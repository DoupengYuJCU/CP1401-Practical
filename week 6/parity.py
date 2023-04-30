def main():
    number = get_number("Enter number: ")
    remainder = calculate_number(number)
    print(f"Parity of {number} should be {remainder}")


def get_number(prompt):
    figure = int(input(prompt))
    return figure


def calculate_number(number):
    return number % 2


def get_word(prompt):
    figure = str(input(prompt))
    return figure


def main():
    number = get_number("Enter number: ")
    name = get_word("Enter Your name: ")
    remainder = calculate_number(number)

    if remainder == 0:
        print(name.lower())
    elif remainder == 1:
        print(name.upper())


main()
