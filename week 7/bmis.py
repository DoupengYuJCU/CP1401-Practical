""" BMIs """
import numpy


def main():
    """runs through a number of weights for a 1.75m person and calculate the BMI"""
    fixed_height = 1.75
    for weight in range(50, 101, 2):
        bmi = calculate_bmi(fixed_height, weight)
        category = determine_weight_category(bmi)
        print(f"Height {fixed_height}m, Weight {weight}kg = BMI {bmi:.1f}, considered {category:1}")


def calculate_bmi(fixed_height, weight):
    return weight / (fixed_height ** 2)


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


def main2():
    """varying heights as well as weights"""
    for height in numpy.arange(1.5, 2.0, 0.1):
        for weight in range(50, 101, 10):
            bmi = calculate_bmi(height, weight)
            category = determine_weight_category(bmi)
            print(f"Height {height:.1f}m, Weight {weight:3}kg = BMI {bmi:.1f}, considered {category:1}")


main2()