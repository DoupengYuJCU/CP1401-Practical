def main():
    height = get_valid_number("Height (m): ", 0, 3)
    weight = get_valid_number("Weight (kg): ", 0, 300)
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print(f"This BMI is {bmi}, which is considered {category}")


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def determine_weight_category(bmi):
    if bmi < 18.2:
        return "underweight"
    elif bmi < 25:
        return  "normal"
    elif bmi < 30:
        return  "overweight"
    else:
        return "obese"

# def run_tests():
#     height = get_valid_number("height m:", 0, 3)
#     print(height)
#     weight = get_valid_number("weight kg: ", 0, 300)
    # print(weight)


def calculate_bmi(height, weight):
    return weight / (height ** 2)

# run_tests()


main()
