def question_1():
    print_line(40)


def print_line(length):
    print("-" * length)


question_1()


def question_2():
    some_number = int(input("Number: "))
    if is_even(some_number):
        print(f"{some_number} is even")
    else:
        print(f"{some_number} is odd")


def is_even(number):
    return number % 2 == 0


question_2()


def question_3():
    name = get_valid_input("Your name: ")
    place_of_birth = get_valid_input("Your birth place: ")
    print(f"Hi {name} from {place_of_birth}!")


def get_valid_input(prompt):
    users_input = input(prompt)
    while users_input == "":
        print("Invalid input.")
        users_input = input(prompt)
    return users_input


question_3()


def question_4():
    minimum_number = int(input("Minimum number: "))
    maximum_number = int(input("Maximum number: "))
    while maximum_number < minimum_number:
        print(f"Your number must be greater than {minimum_number}.")
        maximum_number = int(input("Maximum number: "))

    whole_numbers = []
    for number in range(minimum_number, maximum_number + 1):
        whole_numbers.append(number)
    print(whole_numbers)


question_4()


def question_5():
    all_subject = []
    subject = input("Enter subject code: ")
    while subject != "":
        if not check_valid(subject):
            print("Invalid subject code.")
        else:
            all_subject.append(subject.upper())
        subject = input("Enter subject code: ")
    print(f"You do these {len(all_subject)} subjects: ")
    all_subject.sort()
    for subject in all_subject:
        print(subject)
    if "CP1401" in all_subject:
        print("You are cool")
    else:
        print("You could be cooler")


def check_valid(subject):
    if len(subject) != 6:
        return False
    if not subject[:2].isalpha():
        return False
    if not subject[2:].isdigit():
        return False
    return True


question_5()