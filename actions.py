import sys
from banking import BankAccount

def exit_program():
    """Terminate banking application"""
    print('Exiting the system... Goodbye!')
    sys.exit(0)
    
def deposit_amount(bank_account: BankAccount):
    try:
        amount = float(input('Enter amount to deposit: '))
        bank_account.add_amount(amount)
        print(f'Depositied ${amount}. \nNew Balance: ${bank_account.balance}\n')
    except ValueError:
        print('Invalid amount. Please enter a number.')