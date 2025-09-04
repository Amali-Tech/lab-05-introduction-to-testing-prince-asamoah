import sys
from banking import BankAccount

def exit_program():
    """Terminate banking application"""
    print('Exiting the system... Goodbye!')
    sys.exit(0)
    
def deposit_amount(bank_account: BankAccount):
    try:
        amount = input('Enter amount to deposit: ')
        bank_account.add_amount(float(amount))
        print(f'Deposited ${float(amount)}.')
        print(f'New Balance: ${bank_account.balance}\n')
    except ValueError:
        print('Invalid amount. Please enter a number.')

def withdraw_amount(bank_account: BankAccount):
    try:
        amount = input('Enter amount to withdraw: ')
        bank_account.withdraw_amount(float(amount))
        print(f'Withdrawn ${amount}.')
        print(f'New Balance: ${bank_account.balance}\n')
        
    except ValueError:
        print('Invalid amount. Please enter a number.')