"""
Personal Expense Tracker

Description:
A command-line application that helps users track and manage their personal expenses.
The application allows users to add expenses, view their spending history, monitor their
budget, and save all transactions to a CSV file for persistent storage.

Features:
1. Add Expenses
   - Record date, category, amount, and description for each expense
   - Input validation for numerical amounts
   - Flexible categorization of expenses

2. View Expenses
   - Display all recorded expenses in a formatted table
   - Show transaction history with details

3. Budget Tracking
   - Set and monitor monthly budgets
   - Calculate remaining budget
   - Alert users when they exceed their budget
   - Display budget statistics

4. Data Persistence
   - Save all expenses to a CSV file
   - Load previous expenses when program starts
   - Automatic data recovery

Technical Implementation:
- Uses CSV file format for data storage
- Implements error handling for robust operation
- Maintains data integrity through proper file operations
- Follows modular design principles

Usage:
1. Run the program
2. Select options from the interactive menu
3. Follow prompts to input or view data
4. Save changes before exiting

Data Structure:
- Expenses stored as dictionaries with fields:
  * date: transaction date
  * category: expense category
  * amount: transaction amount (stored as float)
  * description: additional details

Requirements:
- Python 3.x
- CSV module (built-in)
- OS module (built-in)

File Structure:
- expenses.csv: Data storage file
- expense_tracker.py: Main program file

Author: Scott Hardy
Version: 1.0
"""

import csv, os

# Variables

all_expenses = []
expenses_csv = "expenses.csv"

# Add Expense Function
def add_expense():

    expense = {}
    exp_date = input("What was the date of the expense? Enter date in format YYYY-MM-DD")
    expense["date"] = exp_date
    exp_category = input("Please provide the category of the expense. i.g.: Fuel, Travel, Meal, etc.:")
    expense["category"] = exp_category
    exp_amount = float(input("Please provide the amount of the expense:"))
    expense["amount"] = exp_amount
    exp_desc = input("Please provide a brief description of the expense:")
    expense["description"] = exp_desc
    all_expenses.append(expense)

# View Expenses Function
def view_expenses():

    for x in all_expenses:
        print("-----")
        if x["date"] != '':
            print(f"Expense Date: {x['date']}")
        else:
            print("Expense date is missing")
        if x["category"] != '':
            print(f"Expense Category: {x['category']}")
        else:
            print("Expense category is missing")
        if x["amount"] != '':
            print(f"Expense Amount: {x['amount']}")
        else:
            print("Expense amount is missing")
        if x["description"] != '':
            print(f"Expense Description: {x['description']}")
        else:
            print("Expense description is missing")

# Track Budget Function
def track_budget():

    try:
        budget = float(input("Please enter a budget amount for the month:"))
        total_expenses = 0

        for x in all_expenses:
            total_expenses += float(x["amount"])

        if budget < 0:
            print("Budget cannot be negative.")
        elif budget <= total_expenses:
            print(f"You have exceeded your budget by {round(total_expenses - budget, 2)}")
        elif budget == total_expenses:
            print("You mave met your budget.")
        else:
            print(f"You have ${round(budget - total_expenses,2 )} left for the month")

    except ValueError:
        print("Please enter a valid number")

# Save Expenses Function
def save_expenses():

    field_names = ["date", "category", "amount", "description"]

    if not os.path.exists(expenses_csv):

        with open(expenses_csv, "x") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(all_expenses)

    else:

        with open(expenses_csv, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(all_expenses)

# Load Expenses Function
def load_expenses():

    if not os.path.exists(expenses_csv):

        field_names = ["date", "category", "amount", "description"]

        with open(expenses_csv, "x") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(all_expenses)

    else:

        with open("expenses.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for lines in reader:
                all_expenses.append(lines)

# Interactive Menu Function
def menu():

    load_expenses()

    run_program = True

    while run_program:

        print("\nExpense Tracker Menu:")
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")

        try:
            choice = int(input("Please enter one of the options below:"))

            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                track_budget()
            elif choice == 4:
                save_expenses()
            elif choice == 5:
                print("Exiting program")
                run_program = False
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")


menu()