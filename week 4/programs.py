"""
1.Error Checking
get worker_level
while worker_level<1 or worker_level>10
    display Invalid Worker Level
get worker_level
total_salary=worker_level*5000
    display With worker level worker_level, your salary is $total_salary"
"""
BASE_PAY = 5000
worker_level = int(input("worker level:"))
while worker_level < 1 or worker_level > 10:
    print("Invalid Worker Level")
worker_level = int(input("worker level:"))
total_salary = worker_level*BASE_PAY
print(f"With worker level{worker_level},your salary is${total_salary:,.2f}")

""""
2.Number Sequences
"""
"""a."""
for number in range(1,101):
    if number % 2==1:
        print(number)
"""b."""
for Summer_Olympic in range(1986,2023,4):
    print(Summer_Olympic," ",end="\t")
"""c."""
for Winter_Olympic in range (1924, 2023, 4):  # Winter Olympic Games held every four years
    print(Winter_Olympic, end=' ')
print()


"""
3.Menus
display menu
get users_choice
while users_choice != q
    if choice == S
        display smiley face
    else if choice == f
        display frowny face
    else
        display error message
    display menu
    get users_choice
if users_choice == q
    display Farewell
"""
print("Menu: (S)miley,(F)rowny,(Q)uit")
users_choice = str(input("Your choice is(s, f or q): "))
while users_choice != 'q':
    if users_choice == 's':
        print("Smiley face")
    elif users_choice == 'f':
        print("Frowny face")
    else:
        print("Error message")
    print("Menu: (S)miley,(F)rowny,(Q)uit")
    users_choice = str(input("Your choice is(s, f or q): "))
if users_choice == 'q':
    print("Farewell")

"""
4.Accumulation
Average Age
get age
while age != -1
total_age= total_age + age
count = count + 1
get age
average = total_age / count
display total_age
display average
display count
"""
sentinel = 0
total_age = 0
count = 0
age = int(input("Enter age: "))
while age != -1:
    total_age += age
    count += 1
    age = int(input("Enter age: "))
average = total_age / count
print(total_age)
print(average)
print(count)

"""Smileys Count
smile_count = 0
frown_count = 0
display menu
get users_choice
while users_choice != q
    if choice == S
    smile_count += 1
        display smiley face
    else if choice == f
    frown_count += 1
        display frowny face
    else
        display error message
    display menu
    get users_choice
if users_choice == q
    display Farewell
    display smile_count,frown_count
"""
smile_count = 0
frown_count = 0
print("Menu: (S)miley,(F)rowny,(Q)uit")
users_choice = str(input("Your choice is(s, f or q): "))
while users_choice != 'q':
    if users_choice == 's':
        smile_count += 1
        print("Smiley face")
    elif users_choice == 'f':
        frown_count += 1
        print("Frowny face")
    else:
        print("Error message")
    print("Menu: (S)miley,(F)rowny,(Q)uit")
    users_choice = str(input("Your choice is(s, f or q): "))
if users_choice == 'q':
    print("Farewell")
    print('You have printed', smile_count, 'smiles', 'and', frown_count, 'frownies', sep=' ')

"""Guessing Gamne
SECRET = 6
guess = int(input("Guess a number: "))
guessNumb = 1
get guess
while guess not 6
    if guess > 6
        display Higher
    else if guess < 6
        display Lower
    display Guess Again!
    get guess
guess_number = guess_number + 1
display You got it in guess_number guesses
    
"""
SECRET = 6
guess = int(input("Guess a number: "))
guessNumb = 1

while guess != SECRET:
    if guess > SECRET:
        print("Higher")
    elif guess < SECRET:
        print("Lower")
    print("Guess again!")
    guess = int(input("Guess a number: "))
    guessNumb += 1
print("You get it in "+ str(guessNumb) + " guesses !")

"""Total Numbers
total_number = 0
get number_amount
repeat number_amount times
    get number
    total_number = total_number + number
    display number_amount,total_number
"""
total_number = 0
number_amount = int(input("How many numbers do you want to add up? "))
for i in range(number_amount):
    number = int(input("Enter number " + str(i + 1) + ': '))
    total_number += number
print("The total of those", number_amount, "numbers is", total_number)


#6.Nested Loops
""""
get users_rows, users_columns
for columns in range (1, users_rows + 1)
    for rows in range(0, users_columns)
        display rows
"""
users_rows = int(input("Rows: "))
users_columns = int(input("Columns: "))
for columns in range(1, users_rows + 1):
    for rows in range(0, users_columns):
        print(rows, end=" ")
    print()