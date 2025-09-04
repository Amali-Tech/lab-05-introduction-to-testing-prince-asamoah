class BankAccount:
    """
    A simple bank account class supporting adding and withdrawing money from account.
    
    Attributes:
        balance (float): The current balance of the account. Defaults to 0.
    """
    
    def __init__(self):
        """Initialize the BankAccount with a starting balance of 0."""
        self.balance = 0