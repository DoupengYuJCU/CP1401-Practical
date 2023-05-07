""" Seconds """


def main():
    """display value in minutes and seconds."""
    for seconds in range(0, 3176, 635):
        convert_time = calculate_time(seconds)
        print(f"{seconds} seconds is {convert_time}")
    duration_in_seconds = get_duration_in_seconds()
    love_time = calculate_time(duration_in_seconds)
    print(f"You love {love_time}")


def calculate_time(seconds):
    number = f"{seconds // 60}m {seconds % 60}s"
    return number


def get_duration_in_seconds():
    number = int(input("Favourite duration in seconds: "))
    return number


main()