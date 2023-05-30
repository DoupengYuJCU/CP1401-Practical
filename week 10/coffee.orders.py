import random
MENU = "(O)rder - (D)rink - (R)andom choice - (Q)uit"
COFFEES = ["Flat White", "Espresso", "Long Black", "Babyccino"]


def main():
    print("Welcome to the IT@JCU Coffee Shop")
    print(MENU)
    users_choice = input(">>> ").upper()
    while users_choice != "Q":
        if users_choice == "O":
            coffee_order = get_coffee()
            choose_types(coffee_order)
        elif coffee_order == "D":
            if coffee_order == "":
                print("Oh... Where's my coffee?")
            else:
                print(f"Hmm, nice{coffee_order}")
        elif coffee_order == "R":
            coffee_order = random.choice(COFFEES)
            choose_types(coffee_order)
        else:
            print("Invalid option")
        print(MENU)
        users_choice = input(">>> ").upper()
    print("Thanks for drinking coffee")


def get_coffee():
    print("Please choose from: ")
    for coffee in COFFEES:
        print(coffee, end="-")
    coffee_order = input("? ").title()
    while coffee_order not in COFFEES:
        print("Invalid order.")
        coffee_order = input("? ").title()
    return coffee_order


def display_types(coffee_order):
    print(f"Here's how to make a/n {coffee_order}")
    if coffee_order == "Espresso":
        mill_beans()
        make_espresso()
    elif coffee_order == "Long Black":
        mill_beans()
        make_espresso()
        hot_water()
    elif coffee_order == "Flat white":
        mill_beans()
        make_espresso()
        blended_milk()
    elif coffee_order == "Babyccino":
        blended_milk()
    else:
        print("Something went wrong! Unknown coffee.")


def hot_water():
    print("- Add hot water to cup")


def mill_beans():
    print("- Insert portafilter into grinder")
    print("- Press grind button to grind beans into portafilter")


def make_espresso():
    print("- Distribute grounds")
    print("- Tamp grounds")
    print("- Insert full portafilter into group head")
    print("- Press shot button to pour espresso into cup")


def blended_milk():
    print("- Fill jug with milk")
    print("- Steam milk until nice microfoam formed and milk up to temperature")
    print("- Swirl milk gently in jug")
    print("- Pour milk into cup... carefully, artistically :)")