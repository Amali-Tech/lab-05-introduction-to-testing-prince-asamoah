import unittest
from banking import BankAccount

class TestGenerateSummary(unittest.TestCase):
    def setUp(self) -> None:
        """Create a new account for each test"""
        self.account = BankAccount()
        
    def tearDown(self) -> None:
        del self.account
        