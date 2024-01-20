import csv
from datetime import datetime

def add_transaction():
    date = input("Enter the date (YYYY-MM-DD): ")
    t_type = input("Type (income/expense): ").lower()
    category = input("Category: ")
    amount = float(input("Amount: "))

    with open('transactions.csv', 'a', newline='') as file:  # newline='' makes sure that the csv reader / writer functions handle the newline characters themselves
        writer = csv.writer(file)
        writer.writerow([date, t_type, category, amount])

def summarize_transactions():
    with open('transactions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip the the top / header row
        income = expense = 0
        for row in reader:
            if row[1] == 'income':
                income += float(row[3])
            elif row[1] == 'expense':
                expense += float(row[3])
        print(f"Total Income: {income}")
        print(f"Total Expense: {expense}")
        print(f"Net Income: {income - expense}")

def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add a transaction")
        print("2. Summarize transactions")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            summarize_transactions()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

def start_of_csv():
    try:
        with open('transactions.csv', 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount (without $ sign)"])
    except FileExistsError:
        pass  # File already exists, no need to create it again

start_of_csv()

