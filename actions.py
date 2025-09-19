from typing import Optional
from logger import LoggerService, LogLevel


def deposit_amount(account, logger: Optional[LoggerService] = None):
    amount = float(input("Enter amount to deposit: "))
    try:
        account.add_amount(amount)
        amt_str = f"{float(amount)}"
        if logger:
            logger.log(f"Deposited ${amt_str}")
        print(f"Deposited ${amt_str}. New Balance: ${float(account.balance)}")
    except ValueError as e:
        if logger:
            logger.log(str(e), LogLevel.ERROR)
        print(f"Error: {e}")


def withdraw_amount(account, logger: Optional[LoggerService] = None):
    amount = float(input("Enter amount to withdraw: "))
    try:
        account.withdraw_amount(amount)
        amt_str = f"{float(amount)}"
        if logger:
            logger.log(f"Withdrew ${amt_str}")
        print(f"Withdrawn ${amt_str}. New Balance: ${float(account.balance)}")
    except ValueError as e:
        if logger:
            logger.log(str(e), LogLevel.ERROR)
        print(f"Error: {e}")


def show_summary(account, logger: Optional[LoggerService] = None):
    summary = account.generate_summary()
    if logger:
        logger.log("Generated account summary")
    print(summary)


def exit_program():
    print("Thank you for banking with us!")
    exit(0)
