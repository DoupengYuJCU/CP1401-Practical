# Debug program 1 - friends' names
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(0, len(names)):
    print(f"{i + 1}. {names[i]}")
last_number = len(names)
print(f"The last name (number {last_number}) is {names[last_number - 1]}")

# Problem(s) for program 1:
# out of range

# Fixed code for program 1:
# print(f"{i + 1}. {names[i]}")
# {names[last_number - 1]}

# Debug program 2 - title-casing country names
countries = ["australia", "new zeaLAND", "India"]
for i in range(len(countries)):
    countries[i] = countries[i].title()
print(countries)  # country names should be in title-case now

# Problem(s) for program 2:
# 'tuple' object does not support item assignment

# Fixed code for program 2:
# ['Australia', 'New Zealand', 'India']