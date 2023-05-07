"""Dog years"""
First_Human_Year = 10.5
After_Human_Year = 4
CONSTANT_NUMBER = 2


def main():
    """calculate a dog's age in dog years"""
    human_years = get_number("Age in human year is: ")
    category = determine_dog_years(human_years)
    print(f"Age in dog years is {category}")


def get_number(prompt):
    age = int(input(prompt))
    return age


def determine_dog_years(human_years):
    """Determining dog's age by human age"""
    if human_years <= CONSTANT_NUMBER:
        dog_years = human_years * First_Human_Year
    else:
        dog_years = (First_Human_Year * CONSTANT_NUMBER) + After_Human_Year * (human_years - CONSTANT_NUMBER)
    return dog_years


main()