# A simple terminal-based banking app.
# Allows the user to deposit and withdraw amount from a bank account.

from banking import BankAccount
from actions import exit_program, deposit_amount


def main():
    """Banking application starts here"""

    # Create a new bank account
    account = BankAccount()
    actions = {"1": lambda: deposit_amount(account), "2": lambda: exit_program()}

    print("\n=== Welcome to Pacifica Bank ===\n")

    while True:

        print("Choose an option:")
        print("1. Deposit")
        print("2. Exit")
        print("")

        choice = input("Enter your choice (1-2): ").strip()

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please Select 1 - 2. \n")


if __name__ == "__main__":
    main()
