import csv
import os

# File to store expenses
csv_filename = "expenses.csv"

def init_csv():
    """Create the expenses CSV file with headers if it doesn't exist."""
    if not os.path.exists(csv_filename):
        with open(csv_filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Payment Method", "Amount"])

def add_expense(date, method, amount):
    """Append a new expense to the CSV file."""
    with open(csv_filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, method, amount])

def read_expenses():
    """Read all expenses from the CSV file."""
    if not os.path.exists(csv_filename):
        return []
    with open(csv_filename, mode="r") as file:
        reader = csv.reader(file)
        return list(reader)
