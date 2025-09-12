import unittest
from banking import BankAccount

class TestGenerateSummary(unittest.TestCase):
    def setUp(self) -> None:
        """Create a new account for each test"""
        self.account = BankAccount()
        
    def tearDown(self) -> None:
        del self.account
        
    def test_summary_after_deposit(self):
        self.account.add_amount(100)
        summary = self.account.generate_summary()
        self.assertEqual(summary, 'Balance: $100.0, Last Transaction: +100.0')
    
    def test_summay_after_withdrawal(self):
        self.account.add_amount(200)
        self.account.withdraw_amount(50)
        summary = self.account.generate_summary()
        self.assertEqual(summary, 'Balance: $150.0, Last Transaction: -50.0' )
        
    def test_summary_after_initial_balance(self):
        test_summary = self.account.generate_summary()
        self.assertEqual(test_summary, 'Balance: $0.0, Last Transaction: None')