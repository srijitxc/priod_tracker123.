import datetime


def get_date_input(prompt):
    while True:
        try:
            date_str = input(prompt + " (YYYY-MM-DD): ")
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid format. Please enter date in YYYY-MM-DD format.")


def predict_period(last_period_date, cycle_length):
    next_period = last_period_date + datetime.timedelta(days=cycle_length)
    ovulation_day = last_period_date + datetime.timedelta(days=cycle_length - 14)
    fertile_start = ovulation_day - datetime.timedelta(days=4)
    fertile_end = ovulation_day + datetime.timedelta(days=1)

    print("\n🩸 Period Prediction Report 🩸")
    print(f"Last Period Start Date : {last_period_date}")
    print(f"Average Cycle Length   : {cycle_length} days")
    print(f"Next Period Expected   : {next_period}")
    print(f"Ovulation Day          : {ovulation_day}")
    print(f"Fertile Window         : {fertile_start} to {fertile_end}")


def main():
    global cycle_length
    print("🌸 Welcome to Period Tracker 🌸\n")
    last_period_date = get_date_input("Enter your last period start date")

    while True:
        try:
            cycle_length = int(input("Enter your average cycle length (e.g., 28): "))
            if 20 <= cycle_length <= 40:
                break
            else:
                print("Please enter a realistic cycle length between 20 and 40.")
        except ValueError:
            print("Please enter a valid number.")

    predict_period(last_period_date, cycle_length)


if __name__ == "__main__":
    main()
