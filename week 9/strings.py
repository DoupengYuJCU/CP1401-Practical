# 1.Processing Strings
def question_1():

    data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                    "Something else that's very important = 9.2%", "x = 42%"]
    for string in data_strings:
        start_str_index = string.find("= ")
        value = float(string[start_str_index + 2:-1])
        print(value)


question_1()


# 2. Date Strings
def question_2():
    CURRENT_YEAR = 2023
    date_of_birth = str(input("DOB(DD/MM/YYYY): "))
    year_born = int(date_of_birth[-4:len(date_of_birth)])
    print(f"You were born in {year_born}")
    print(f"You will turn {CURRENT_YEAR - year_born} in {CURRENT_YEAR}")


question_2()

# 3. Subject Code Strings
def question_3():
    subject_code = input("Enter subject code: ").upper()
    while subject != "":
        while len(subject) != 6:
            print("Invalid input")
            subject = input("Enter subject code: ").upper()
        it_string = ""
        if subject.startswith("CP"):
            it_string = " IT"
        category = determine_subject(subject)
        print(f"That is a {category}{it_string} subject.")
        subject = input("Enter subject code: ").upper()

def determine_subject(subject):
    if subject[2] == "1":
         year = "first-year"
    elif subject[2] == "2":
         year = "second-year"
    elif subject[2] == "3":
         year = "third-year"
    else:
          year = "Masters or other"
    return year


question_3()