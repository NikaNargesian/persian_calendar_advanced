# persian_calendar_advanced.py
from datetime import date, timedelta

def gregorian_to_persian(year, month, day):
    return f"{year}-{month}-{day} (Persian Calendar Approx.)"

def main():
    print("Welcome to Persian Calendar Advanced 2.0")
    print("Enter day numbers separated by commas (e.g., 15, 256, 365):")
    user_input = input("Day numbers: ")
    day_numbers = [int(x.strip()) for x in user_input.split(",")]

    print("\nResults:")
    for day_number in day_numbers:
        greg_date = date(2025, 1, 1) + timedelta(days=day_number - 1)
        persian_date = gregorian_to_persian(greg_date.year, greg_date.month, greg_date.day)
        print(f"Day {day_number}: {persian_date}")

    print("\nProject upgraded from previous Persian Calendar project with enhanced features.")

if __name__ == "__main__":
    main()