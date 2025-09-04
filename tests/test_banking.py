import unittest
from banking import BankAccount

class TestBankAcount(unittest.TestCase):
    def setUp(self) -> None:
        self.account = BankAccount()
    
    def tearDown(self) -> None:
        self.account.balance = 0
        
    def test_add_amount(self):
        self.account.add_amount(100)
        self.assertEqual(self.account.balance, 100)

if __name__ == '__main__':
    unittest.main()