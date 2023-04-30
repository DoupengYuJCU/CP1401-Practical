"""1. Coffee Brew Ratio"""
"""
function main(）
    dose = get_number("Dose (g)")
    harvest = get_number("Yield (g)")
    ratio = calculate_ratio(dose, harvest)
    style = determine_ratio(radio)
    print ratio, style


function get_number(prompt)
    get number
    return number


function ratio
    return harvest/dose


function calculate_ratio(dose, harvest)
     if ratio < 2:
        return "ristretto"
    elif ratio < 3:
        return "normale"
    else:
        return "lungo"


function check_coffee():
    style = determine_coffee_style(1)
    print(style)
    style = determine_coffee_style(2)
    print(style) 
    style = determine_coffee_style(13.5)
    print(style) 


main()   
"""


def main():
    dose = get_number("Dose (g): ")
    harvest = get_number("Yield (g): ")
    ratio = calculate_ratio(dose, harvest)
    style = determine_ratio(ratio)
    print(f"1 : {ratio} is considered {style}")


def get_number(prompt):
    number = float(input(prompt))
    return number


def calculate_ratio(dose, harvest):
    return harvest/dose


def determine_ratio(ratio):
    if ratio < 2:
        return "ristretto"
    elif ratio < 3:
        return "normale"
    else:
        return "lungo"


def check_coffee():
    style = determine_coffee_style(1)
    print(style)  # This should be ristretto
    style = determine_coffee_style(2)
    print(style)  # This should be normale
    style = determine_coffee_style(13.5)
    print(style)  # This should be lungo


main()

