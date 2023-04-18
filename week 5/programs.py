"""
1. Percentage change
get original_value,change
display result=original_value+(original_value * change)
display result
"""
original_value = float(input("Enter your number:"))
change = float(input("Enter your change:"))
result = original_value+(original_value * change)
print("result:",result)
print(f"{original_value},{change},{result}")
"""
2. Time of day
get time 
if time < 12
display before
else
    display after
get choice
if choice = "coming"
display coming hi
else
    display going bye

"""
time = int(input('Input the time (0-23 hours): '))
choice = input('Input if you are coming or going: ').lower()
if time < 12:
    situation = 'before'
else:
    situation = 'after'
if choice == 'coming':
    coming_going = 'coming. Hi'
else:
    coming_going = 'going. Bye'
print(f'It is {situation} noon and you are {coming_going}!')
"""
3. Coffee orders
get coffee_size
if coffee_size = small
    display cost = 3
else if
    coffee_size = medium
    display cost=4
else
    display cost=5
get coffee_color
if coffee_color=black
    display cost
else if
coffee_color=white
    display cost += 1
else
    cost=6
    display cost
"""
coffee_size = input("Enter the chosen size: ").lower()
coffee_color = input("Enter the color: ").lower()
if coffee_size == "small":
    cost = 3
elif coffee_size == "medium":
    cost = 4
else:
    cost = 5
if coffee_color == "black":
    cost = cost
elif coffee_color == "white":
    cost += 1
else:
    cost = 6
print(print(f"Cost:$:{cost}"))

"""
4. Coffee orders with error-checking
get coffee_color
while color != black and color != white
    display invalid
get coffee_size
while size != small and size != medium and size != large
    display invalid
if coffee_size = small
    display cost = 3
else if
    coffee_size = medium
    display cost=4
else
    display cost=5
if coffee_color=black
    display cost
else if
coffee_color=white
    display cost += 1
else
    cost += 1
    display cost
"""

size = input("Enter the chosen size: ").lower()
color = input("Enter the color: ").lower()
while color != "black" and color != "white":
    print("invalid")
    color = input("Enter the color: ").lower()
while size != "small" and size != "medium" and size != "large":
    print("invalid")
    size = input("Enter the chosen size: ").lower()
if size == "small":
    cost = 3
elif size == "medium":
    cost = 4
else:
    cost = 5
if color == "black":
    print(f"cost: ${cost}")
else:
    cost += 1
    print(print(f"cost: ${cost}"))
"""
5. Accumulation
get lower,higher
while higher < lower
for i in range
    display i
    total += i
    display total
"""
lower = int(input("Enter a lower number:"))
higher = int(input("Enter a higher number:"))
total = 0
while higher < lower:
    print("Invalid")
    lower = int(input("Enter a lower number:"))
    higher = int(input("Enter a higher number:"))
for i in range(lower,higher+1):
    print(i, end=" ")
    total += i
print(f"total:{total} ")




