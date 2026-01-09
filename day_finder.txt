# Python Day Finder - Team Project
# Displays the day of the week for a given date

import datetime

def find_day(day, month, year):
    date = datetime.date(year, month, day)
    return date.strftime("%A")

def main():
    print("=" * 40)
    print("   PYTHON DAY FINDER")
    print("=" * 40)

    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))

    result = find_day(day, month, year)
    print(f"\nThe day is: {result}")

if __name__ == "__main__":
    main()
