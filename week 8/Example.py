places = []
place = input("Place: ")
while place != "":
    places.append(place)
    place = input("Place: ")
print("On my holiday, I went to: ")
for place in places:
    longest_place = max(places)
    print(place)
print(f"The place with the longest name was {longest_place}.")