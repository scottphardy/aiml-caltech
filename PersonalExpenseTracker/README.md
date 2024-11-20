# Personal Expense Tracker
### Caltech AI Bootcamp - Programming Refresher

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
