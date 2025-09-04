class BankAccount:
    """
    A simple bank account class supporting adding and withdrawing money from account.
    
    Attributes:
        balance (float): The current balance of the account. Defaults to 0.
    """
    
    def __init__(self):
        """Initialize the BankAccount with a starting balance of 0."""
        self.balance = 0
        
    def add_amount(self, amount: float):
        """
        Deposit amount into account.
        
        Args:
            amount (float): The amount to deposit.
            
        Returns:
            None
        """
        
        # Increase balance by the deposit amount
        self.balance += amount
        
    def withdraw_amount(self, amount: float):
        """
        Withdraw amount from account.

        Args:
            amount (float): The amount to withraw.
            
        Returns:
            None
        """
    
        # Decrease balance by the withdrawal amount
        self.balance -= amount
        
        