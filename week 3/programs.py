
"""
1.Tax
get income
if income<100
    total_tax=0
    elif income >= 100 and income<1000
    total_tax=ncome*0.05
else:
    total_tax=income*0.1

    take_home_pay=income-tax_rate
    display Python Party Tax Program-Where Tax is a Party
    display Total tax is:$,total_tax
    display Take home pya is:$,take_home_pay,
"""


TAX_RATE_LOW = 0.05  # 5%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_MEDIUM = 500
TAX_THRESHOLD_HIGH = 1000

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))
if income < TAX_THRESHOLD_LOW:
    total_tax = 0
elif TAX_THRESHOLD_LOW <= income < TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_LOW

elif income > TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_HIGH
else:
    total_tax = income * TAX_THRESHOLD_MEDIUM
    take_home_pay = income - total_tax
    print("Total tax is: $", total_tax, sep="")

    print("Take home pay is: $", take_home_pay, sep="")

"""
2.Car Insurance
get Age
if Age<18:
    display Hire refused
elif Age<25:
    display Insurance required
else:
    display Insurance not required
    """

HIRE_REFUSED = 18
INSURANCE_REQUIRED = 25
age = input("Age: ")
if age < HIRE_REFUSED:
    print("Hire refused")
elif age < INSURANCE_REQUIRED:
    print("Insurance required")
else:
    print("Insurance not required")

""""
3.Simple Password Checker
get password
if password == PASSWORD:
    display Access Granted
else:
    display Access Denied
    """

PASSWORD = "PASSWORD"
password = str(input("Enter Password"))
if password == PASSWORD:
    print("Access Granted")
else:
    print("Access Denied")

"""""
4.Dog Year
get first_human_year,after_human_year
if age = 1 or 2
    returnAge=first_human_year*age
else:
    returnAge = (age-2)*after_human_year+(first_human_year*2)
display dog_year
"""


First_Human_Year = 10.5
After_Human_Year = 4

age = int(input("Age in human years: "))
returnAge = 0
if age == 1 or age == 2:
    returnAge = First_Human_Year*age
else:
    returnAge = (age - 2) * After_Human_Year + (First_Human_Year * 2)
print("Age in dog years is  ", returnAge, sep='')


"""5.Rock of Ages
get age
if age > 120 and age < 0
    display Invalid_age
if 0 >= age < 18
    display engineer
if 18 >= age < 30
    display youth
if 30 >= age < 50
    display Middle_age
if age >= 50
    display Elderly
"""

age = float(input("your age is"))
if(120 < age) and (0 > age):
    print("Invalid age")
if 0 < age < 18:
    print("engineer")
if age < 30:
    print("Youth")
if age < 50:
    print("Middle age")
else:
    print("Elderly")

"""6.Speeding Fines
get speed,speed_limit
exceed=speed-speed_limit
if speed > speed_limit
else if exceed<13
    display penalty_amount=177
else if 13 <= exceed <= 20
    display penalty_amount=266
else if 20 < exceed <= 30
    display penalty_amount=444
else if 30 < exceed <= 40
    display penalty_amount=622
else:
    display penalty_amount=1245
    display penalty_amount
"""
speed_limit = float(input("the speed limit is:"))
speed = float(input("speed is:"))
excess = speed - speed_limit
if excess <= 0:
    print("penalty_amount = 0")
elif 13 < excess:
    print("penalty_amount = 177")
elif excess <= 20:
    print("penalty_amount = 266")
elif excess <= 30:
    print("penalty_amount = 444")
elif excess <= 40:
    print("penalty_amount = 622")
else:
    print("penalty_amount = 1245")
    print("the penalty amount is", result)






