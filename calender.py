import calendar

def display_calendar():
    print("Welcome to the Calendar Program")
    while True:
        print("\nOptions:")
        print("1. View calendar for a specific month")
        print("2. View calendar for a specific year")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            try:
                year = int(input("Enter the year (e.g., 2024): "))
                month = int(input("Enter the month (1-12): "))
                if 1 <= month <= 12:
                    print("\n", calendar.month(year, month))
                else:
                    print("Invalid month! Please enter a number between 1 and 12.")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        elif choice == '2':
            try:
                year = int(input("Enter the year (e.g., 2024): "))
                print("\n", calendar.TextCalendar().formatyear(year, 2, 1, 1, 3))
            except ValueError:
                print("Invalid input! Please enter a numeric value for the year.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    display_calendar()
