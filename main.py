# A simple terminal-based banking app.
# Allows the user to deposit and withdraw amount from a bank account.
from banking import BankAccount

def main():
    """Banking application starts here"""
    
    # Create a new bank account
    account = BankAccount()
    
    print(f'Current Balance: ${account.balance}')


if __name__ == "__main__":
    main()
