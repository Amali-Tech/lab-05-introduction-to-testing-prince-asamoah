from typing import Optional
from logger import LoggerService, LogLevel


def deposit_amount(account, logger: Optional[LoggerService] = None):
    amount = float(input("Enter amount to deposit: "))
    try:
        account.add_amount(amount)
        if logger:
            logger.log(f"Deposited ${amount}")
        print(f"Deposited ${amount}. New Balance: ${account.balance}")
    except ValueError as e:
        if logger:
            logger.log(str(e), level=LogLevel.ERROR)
        print(f"Error: {e}")

def withdraw_amount(account, logger: Optional[LoggerService] = None):
    amount = float(input("Enter amount to withdraw: "))
    try:
        account.withdraw_amount(amount)
        if logger:
            logger.log(f"Withdrew ${amount}")
        print(f"Withdrawn ${amount}. New Balance: ${account.balance}")
    except ValueError as e:
        if logger:
            logger.log(str(e), level=LogLevel.ERROR)
        print(f"Error: {e}")

def show_summary(account, logger: Optional[LoggerService] = None):
    summary = account.generate_summary()
    if logger:
        logger.log("Generated account summary")
    print(summary)

def exit_program():
    print("Thank you for banking with us!")
    exit(0)
