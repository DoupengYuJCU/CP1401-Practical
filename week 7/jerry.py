"""
function main
    speed_in_mph = get_valid_number("speed in mph")
    speed_limit_in_kph = get_valid_number("speed limit in kph")
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    fine = determine_fine(speed_in_km, speed_limit_in_kph)
    print fine
"""
CONVERSION_RATE = 0.621371
SPEED_MINIMUM = 0
LOW_SPEED = 13
MEDIUM_SPEED = 20
HIGH_SPEED = 30
SPEED_MAXIMUM = 40


def main():
    """Calculate the fine according to user's speed and speed limit"""


def main():
    """Calculate the fine according to user's speed and speed limit"""
    speed_in_mph = get_valid_number("speed in mph: ")
    speed_limit_in_kph = get_valid_number("speed limit in kph: ")
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    fine = determine_fine(speed_in_kph, speed_limit_in_kph)
    print(f"Fine: {fine}")


def get_valid_number(prompt):
    """Get user's speed and speed limit"""
    number = float(input(prompt))
    return number


def convert_miles_to_km(speed_in_mph):
    rate = CONVERSION_RATE
    return speed_in_mph / rate


def determine_fine(speed_in_kph, speed_limit_in_kph):
    """Determine the final fine"""
    speed_exceeded = speed_in_kph - speed_limit_in_kph
    if speed_exceeded <= SPEED_MINIMUM:
        fine = 0
    elif speed_exceeded < LOW_SPEED:
        fine = 177
    elif speed_exceeded < MEDIUM_SPEED:
        fine = 266
    elif speed_exceeded < HIGH_SPEED:
        fine = 444
    elif speed_exceeded < SPEED_MAXIMUM:
        fine = 622
    else:
        fine = 1245
    return fine


main()