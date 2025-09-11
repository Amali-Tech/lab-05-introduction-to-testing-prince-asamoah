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
        
    def test_add_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.account.add_amount(0)
            
    def test_add_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.account.withdraw_amount(-100)
            
    def test_withdraw_zero_raises_value_error(self):
        self.account.add_amount(100)
        with self.assertRaises(ValueError):
            self.account.withdraw_amount(0)
            
    def test_withdraw_negative_raises_value_error(self):
        self.account.add_amount(100)
        with self.assertRaises(ValueError):
            self.account.withdraw_amount(-10)
            
    def test_overdraft_raises_value_error(self):
        self.account.add_amount(100)
        with self.assertRaises(ValueError):
            self.account.withdraw_amount(200)

if __name__ == '__main__':
    unittest.main()