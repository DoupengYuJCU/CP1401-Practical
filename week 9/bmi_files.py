def main():
    number_people = int(input("Enter the number of people: "))
    out_file = open("bmi.txt", 'w')
    for i in range(1, number_people):
        user_height = float(input("Enter your height(m): "))
        user_weight = float(input("Enter your weight(kg): "))
        bmi = calculate_bmi(user_height, user_weight)
        category = determine_weight_category(bmi)
        out_file.write(f"BMI {bmi:.1f}, considered {category}\n")
    out_file.close()


def calculate_bmi(user_height, weight):
    return weight / (user_height ** 2)


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


main()
