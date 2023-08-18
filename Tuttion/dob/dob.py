from datetime import datetime

def days(dob):
    today = datetime.now()
    dob_date = datetime.strptime(dob, '%Y-%m-%d')
    days_alive = (today - dob_date).days
    return days_alive

dob = input("Enter your date of birth (YYYY-MM-DD): ")
days_alive = days(dob)
print("You have been alive for", days_alive, "days.")
