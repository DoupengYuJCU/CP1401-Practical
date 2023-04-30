import random


def main():
    users_score = get_number("Enter your score: ", 0, 100)
    users_level = total_score(users_score)
    print(f"The score {users_score} is {users_level}")
    random_scores()


# print(f"{value} = {users_level}")


def get_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid")
        number = float(input(prompt))
    return number


def total_score(users_score):
    if users_score < 50:
        return "F"
    elif users_score < 65:
        return "P"
    elif users_score < 75:
        return "C"
    elif users_score < 85:
        return "D"
    else:
        return "HD"


def random_scores():
    total_random_Numb = int(input("How many random scores:"))

    for i in range(total_random_Numb):
        users_score = random.randint(1, 100)
        level = total_score(users_score)
        print(f"{users_score} = {level}")


# run_tests()
main()