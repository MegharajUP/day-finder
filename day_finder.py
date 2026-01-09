import datetime

def find_day(day, month, year):
    """Return the day of the week for a given date."""
    date = datetime.date(year, month, day)
    return date.strftime("%A")

def show_today_day():
    """Return today's day of the week."""
    today = datetime.date.today()
    return today.strftime("%A")

def main():
    print("=" * 40)
    print("   PYTHON DAY FINDER")
    print("=" * 40)
    print("1. Find day for given date")
    print("2. Show today's day")
    
    choice = input("Enter choice (1 or 2): ")
    
    if choice == '1':
        day = int(input("Enter day: "))
        month = int(input("Enter month: "))
        year = int(input("Enter year: "))
        print("Day:", find_day(day, month, year))
    elif choice == '2':
        print("Today is:", show_today_day())
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()