"""""
display Menu
get users_choice
while users_choice not q
    if users_choice = i
        display Instructions
    else if users_choice = c
        get number_products
        while number_products < 0
            display Invalid choice
            get number_products
        get price_wanted
        while price_wanted <= 0
            display Invalid choice
            get price_wanted
        if number_products > 5
            total_price = number_products * (price_wanted - price_wanted * discount)
        else
            total_price = number_products * price_wanted
        display number_products, price_wanted, total_price
    else
        display Invalid choice
    display Menu
    get users_choice
display Farewell
"""
discount = 0.1
LIMITED_NUMBER = 5
print("Menu: \n(I)nstructions\n(C)alulate\n(Q)uit")
users_choice = str(input("Choice:")).lower()
while users_choice != "q":
    if users_choice == "i":
        print("Enter the number of products you want to buy and your chosen price.")
        print("If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")
    elif users_choice == "c":
        number_products = int(input("Number of products: "))
        while number_products < 0:
            print("Invalid choice")
            number_products = int(input("Number of products: "))
        price_wanted = float(input("Price: "))
        total_price = 0
        while price_wanted <= 0:
            print("Invalid choice")
            price_wanted = float(input("Price: "))
        if number_products > LIMITED_NUMBER:
            total_price = number_products * (price_wanted - price_wanted * discount)
        else:
            total_price = number_products * price_wanted
        print(f"{number_products} * ${price_wanted:,.2f} products = ${total_price:,.2f}")
    else:
        print("Invalid choice")
    print("Menu: \n(I)nstructions\n(C)alulate\n(Q)uit")
    users_choice = input("Choice:").lower()
print("Farewell")

