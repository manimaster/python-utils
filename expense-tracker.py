"""
Expense Tracker

This script allows users to track their expenses and view their spending history.
"""

expenses = []

def add_expense(description, amount):
    expenses.append({"description": description, "amount": amount})

def view_expenses():
    total = 0
    for expense in expenses:
        print(f"{expense['description']}: ${expense['amount']}")
        total += expense['amount']
    print(f"Total Expenses: ${total}")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        desc = input("Enter expense description: ")
        amt = float(input("Enter expense amount: $"))
        add_expense(desc, amt)
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        break
