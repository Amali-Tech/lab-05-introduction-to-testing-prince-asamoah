import unittest
from banking import BankAccount

class TestBankAcount(unittest.TestCase):
    def setUp(self) -> None:
        """Set up a new bank account before each test"""
        self.account = BankAccount()
    
    def tearDown(self) -> None:
        """Clean up after each test"""
        del self.account
        
    def test_add_amount(self):
        self.account.add_amount(100)
        self.assertEqual(self.account.balance, 100)
        
    def test_withdraw_amount(self):
        self.account.add_amount(100)
        self.account.withdraw_amount(50)
        self.assertEqual(self.account.balance, 50 )
        

if __name__ == '__main__':
    unittest.main()