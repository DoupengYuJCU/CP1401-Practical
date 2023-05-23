
"""
in_file = open("scores.txt", 'r')
for line in in_file:
    score = float(line)
    total += score
    count += 1
in_file.close()
average = total / count
print(f"Average = {average:.1f}")
"""
total = 0.0
count = 0

file_name = input("Enter your file name: ")
in_file = open("file_name", 'r')
for line in in_file:
    score = float(line)
    total += score
    count += 1
    print(f"Score = {score:4.1f}     Total so far = {total:6.1f}")
in_file.close()
average = total / count
print(f"Average = {average:.1f}")