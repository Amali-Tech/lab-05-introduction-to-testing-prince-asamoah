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
        