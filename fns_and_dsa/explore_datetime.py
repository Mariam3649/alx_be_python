from datetime import datetime, timedelta


def display_current_datetime():
    # Save the current date inside a variable
    current_date = datetime.now()
    # Format the date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date():
    try:
        # Ask user for number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        # Save the future date inside a variable
        future_date = current_date + timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()

