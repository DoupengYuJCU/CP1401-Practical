"""
def main():
    grades = empty list
    for i in range(4):
        get score
        add score to grades
    for j in grades:
        category = determine_score
        print score, category
    print average score
    average = sum(grades) / len(grades)
    trend = identify_trend(grades, average)
    print trend

def get_score(keys, low, high):
    get number
    while number < low or number > high:
        print Invalid number
        get number
    return number

def determine_score(j):
    if j > 85:
        return "HD"
    elif j > 75:
        return "D"
    elif j > 65:
        return "C"
    elif j > 50:
        return "P"
    else:
        return "F"

def identify_trend(grades, average):
    if grades[-1] > average:
        return "positive"
    else:
        return "negative"

"""


CONSTANT_NUMBER = 4


def main():
    grades = []
    for i in range(CONSTANT_NUMBER):
        test_scores = get_score("Score: ", 1, 100)
        grades.append(test_scores)
    for j in grades:
        category = determine_score(j)
        print(f"Score: {j}, which is {category}")
    print(f"The average score was: {sum(grades) / len(grades):.2f}")


def get_score(keys, low, high):
    number = float(input(keys))
    while number < low or number > high:
        print("Invalid number")
        number = float(input([keys]))
    return number


def determine_score(j):
    if j > 85:
        return "HD"
    elif j > 75:
        return "D"
    elif j > 65:
        return "C"
    elif j > 50:
        return "P"
    else:
        return "F"


main()

