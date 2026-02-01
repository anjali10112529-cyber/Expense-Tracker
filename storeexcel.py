import csv
import os

# File to store user signup data
signup_filename = "users.csv"

def init_users_csv():
    """Create the users CSV file with headers if it doesn't exist."""
    if not os.path.exists(signup_filename):
        with open(signup_filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Password"])

def store_data(name, password):
    """Store signup data into users.csv."""
    with open(signup_filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, password])
