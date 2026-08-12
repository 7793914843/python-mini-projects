
expenses = []


# Add Expense
def add_expense():

    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")


# View Expenses
def view_expenses():

    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n========== EXPENSES ==========")

    for i, expense in enumerate(expenses, start=1):

        print("\nExpense", i)
        print("Amount      :", expense["amount"])
        print("Category    :", expense["category"])
        print("Description :", expense["description"])


# Calculate Total
def total_expense():

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense:", total)


# Delete Expense
def delete_expense():

    view_expenses()

    if len(expenses) == 0:
        return

    number = int(input("\nEnter expense number to delete: "))

    if number >= 1 and number <= len(expenses):

        deleted = expenses.pop(number - 1)

        print("Deleted expense:", deleted["description"])

    else:
        print("Invalid expense number.")


# Main Menu
while True:

    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice.")
