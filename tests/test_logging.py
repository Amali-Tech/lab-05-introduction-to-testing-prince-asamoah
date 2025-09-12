import unittest
from unittest.mock import MagicMock
from logger import LoggerService
from banking import BankAccount

class TestBankAccountLogging(unittest.TestCase):
    def setUp(self) -> None:
        """Setup mock logger before each test"""
        self.mock_logger = MagicMock(spec=LoggerService)
        self.account = BankAccount(logger=self.mock_logger)
        
    def tearDown(self) -> None:
        """Reset mock logger and account"""
        self.mock_logger.reset_mock()
        del self.account
    
    def test_deposit_logs_transaction(self):
        self.account.add_amount(100)
        self.mock_logger.log.assert_called_once_with("Deposited $100")
    
    def test_withdraw_logs_transaction(self):
        self.account.add_amount(200)
        self.account.withdraw_amount(50)
        self.mock_logger.log.assert_called_with("Withdrew $50")