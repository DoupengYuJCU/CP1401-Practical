"""4. Read a String from a File"""

def question_4():
    in_file = open("name.txt", "r")
    text = in_file.read().strip()
    in_file.close()
    print(f"Greetings {text}")

question_4()


"""5. Greater-Than Counter"""

count = 0
total_count = 0
file_name = input("Filename: ")
threshold = float(input("Threshold: "))
print("Processing...")
in_file = open(file_name, 'r')

greater_number = 0
content = in_file.readline()
for number in content:
    numbers = float(number)
    if numbers > threshold:
        count += 1
        total_count += 1
in_file.close()


print(f"{count} out of 10 ({count / 10 * 100}%) values in {file_name} are greater than {threshold}")

"""6. File Filter"""

input_filename = input("Input filename: ")
output_filename = input("Output filename: ")
search_string = input("Search string: ")
in_file = open(input_filename, 'r')
out_file = open(output_filename, 'w')

for line in in_file:
    if search_string in line:
        print(line, file=out_file, end="")
in_file.close()
out_file.close()

"""version2"""
input_filename = input("Input filename: ")
output_filename = input("Output filename: ")
in_file = open(input_filename, 'r')
out_file = open(output_filename, 'w')
for line in in_file:
    if line.startswith("So"):
        print(line, file=out_file, end="")
in_file.close()
out_file.close()