"""Calculate salary for worker level"""


def cal_value(worker_level):
    BASE_PAY = 500
    return worker_level * BASE_PAY


def check_value():
    worker_level = int(input("worker level:"))
    while worker_level < 1 or worker_level > 10:
        print("Invalid Worker Level")
        worker_level = int(input("worker level:"))
    return worker_level


def main():
    worker_level = check_value()
    total_salary = cal_value(worker_level)
    print(f"With worker level {worker_level},your salary is ${total_salary:,.2f}")


main()

"""Print grid(rows, columns)"""


def main():
    users_rows = int(input("Rows: "))
    users_columns = int(input("Columns: "))
    grid(users_rows, users_columns)


def grid(users_rows, users_columns):
    for columns in range(1, users_rows + 1):
        for rows in range(0, users_columns):
            print(rows, end=" ")
        print()


main()


