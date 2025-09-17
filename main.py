# A simple terminal-based banking app.
# Allows the user to deposit and withdraw amount from a bank account.

from banking import BankAccount
from actions import exit_program, deposit_amount, withdraw_amount, show_summary
from logger import LoggerService

def main():
    """Banking application starts here"""
    
    # Create logger instance
    logger = LoggerService(name='PacificaBank')
    
    # Create a new bank account
    account = BankAccount()
    actions = {
        "1": lambda: deposit_amount(account, logger),
        "2": lambda: withdraw_amount(account, logger),
        "3": lambda: show_summary(account, logger),
        "4": lambda: exit_program(),
    }

    print("\n=== Welcome to Pacifica Bank ===\n")

    while True:

        print("Choose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Summary")
        print("4. Exit\n")

        choice = input("Enter your choice (1-4): ").strip()

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please Select 1 - 4. \n")


if __name__ == "__main__":
    main()
