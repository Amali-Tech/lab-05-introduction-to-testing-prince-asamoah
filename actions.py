from logger import LoggerService, LogLevel

# Create logger instance
logger = LoggerService(name='PacificaBank')
    
def deposit_amount(account):
    amount = float(input("Enter amount to deposit: "))
    try:
        account.add_amount(amount)
        amt_str = f"{float(amount)}"
        logger.log(f"Deposited ${amt_str}")
        print(f"Deposited ${amt_str}. New Balance: ${float(account.balance)}")
    except ValueError as e:
        logger.log(str(e), LogLevel.ERROR)
        print(f"Error: {e}")


def withdraw_amount(account):
    amount = float(input("Enter amount to withdraw: "))
    try:
        account.withdraw_amount(amount)
        amt_str = f"{float(amount)}"
        logger.log(f"Withdrew ${amt_str}")
        print(f"Withdrawn ${amt_str}. New Balance: ${float(account.balance)}")
    except ValueError as e:
        logger.log(str(e), LogLevel.ERROR)
        print(f"Error: {e}")


def show_summary(account):
    summary = account.generate_summary()
    logger.log("Generated account summary")
    print(summary)


def exit_program():
    print("Thank you for banking with us!")
    exit(0)
