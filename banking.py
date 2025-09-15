from logger import LoggerService, LogLevel

logger = LoggerService(name='Banking')

class BankAccount:
    """
    A simple bank account class supporting adding and withdrawing money from account.
    
    Attributes:
        balance (float): The current balance of the account. Defaults to 0.
    """
    
    def __init__(self):
        """Initialize the BankAccount with a starting balance of 0."""
        self.balance = 0
        self.last_transaction = None
        
    def add_amount(self, amount: float):
        """
        Deposit amount into account.
        
        Args:
            amount (float): The amount to deposit.
            
        Returns:
            None
        """
        
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
        
        # Increase balance by the deposit amount
        self.balance += amount
        self.last_transaction = amount
        
        logger.log(level=LogLevel.INFO, message=f"Deposited ${amount}")
        
    def withdraw_amount(self, amount: float):
        """
        Withdraw amount from account.

        Args:
            amount (float): The amount to withraw.
            
        Returns:
            None
        """

        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive.')
        if amount > self.balance:
            raise ValueError('Insufficient funds. Overdraft not allowed.')
        # Decrease balance by the withdrawal amount
        self.balance -= amount
        self.last_transaction = -amount
        
        logger.log(level=LogLevel.INFO, message=f"Withdrew ${amount}")
        
    def generate_summary(self) -> str:
        """
        Generate a summary of the acount balance and last transaction.
        Returns:
            str: Summary string with balance and last transaction.
        """
        if self.last_transaction is None:
            last_transaction = 'None'
        elif self.last_transaction > 0:
            last_transaction = f'+{float(self.last_transaction)}'
        else:
            last_transaction = str(float(self.last_transaction))
        return f'Balance: ${float(self.balance)}, Last Transaction: {last_transaction}'
        