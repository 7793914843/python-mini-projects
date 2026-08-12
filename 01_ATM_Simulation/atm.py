balance = 10000
pin = 1234


def check_balance():
    print("Your balance is:", balance)


def deposit():
    global balance

    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance = balance + amount
        print("Amount deposited successfully.")
        print("New balance:", balance)
    else:
        print("Invalid amount.")


def withdraw():
    global balance

    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance = balance - amount
        print("Please collect your cash.")
        print("Remaining balance:", balance)


# PIN verification

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:

    print("\nLogin successful!")

    while True:

        print("\n========== ATM ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice.")

else:
    print("Incorrect PIN!")
