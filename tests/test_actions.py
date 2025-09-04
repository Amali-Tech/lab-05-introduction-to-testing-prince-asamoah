import unittest
from unittest.mock import patch
from io import StringIO
from banking import BankAccount
import actions

class TestActions(unittest.TestCase):
    def setUp(self) -> None:
        """Create a new account for each test"""
        self.account = BankAccount()
        
    def tearDown(self) -> None:
        del self.account
    
    @patch('builtins.input', return_value='100')
    @patch('sys.stdout', new_callable=StringIO)
    def test_deposit_amount(self, mock_stdout, mock_input):
        actions.deposit_amount(self.account)
        mock_input.assert_called_once_with('Enter amount to deposit: ')
        self.assertEqual(self.account.balance, 100)
        self.assertIn('Deposited $100.0.', mock_stdout.getvalue())
        self.assertIn('New Balance: $100.0', mock_stdout.getvalue())