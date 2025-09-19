import unittest
from unittest.mock import patch, Mock
from io import StringIO
from banking import BankAccount
import actions
from logger import LoggerService, LogLevel

class TestActions(unittest.TestCase):
    def setUp(self) -> None:
        self.account = BankAccount()
        self.logger = Mock(spec=LoggerService)
        
    def tearDown(self) -> None:
        del self.account
        self.logger.reset_mock()
    
    @patch('builtins.input', return_value='100')
    @patch('sys.stdout', new_callable=StringIO)
    def test_deposit_amount(self, mock_stdout, mock_input):
        actions.deposit_amount(self.account, self.logger)
        mock_input.assert_called_once_with('Enter amount to deposit: ')
        self.assertEqual(self.account.balance, 100)
        self.assertIn('Deposited $100.0.', mock_stdout.getvalue())
        self.assertIn('New Balance: $100.0', mock_stdout.getvalue())
        self.logger.log.assert_called_with("Deposited $100.0")
        
    @patch('builtins.input', return_value='50')
    @patch('sys.stdout', new_callable=StringIO)
    def test_withdraw_amount(self, mock_stdout, mock_input):
        self.account.add_amount(100) # preload balance
        actions.withdraw_amount(self.account, self.logger)
        mock_input.assert_called_once_with('Enter amount to withdraw: ')
        self.assertEqual(self.account.balance, 50)
        self.assertIn('Withdrawn $50.0.', mock_stdout.getvalue())
        self.assertIn('New Balance: $50.0', mock_stdout.getvalue())
        self.logger.log.assert_called_with("Withdrew $50.0")
        
    @patch('builtins.input', return_value='-50')
    @patch('sys.stdout', new_callable=StringIO)
    def test_deposit_negative_shows_error_message(self, mock_stdout, mock_input):
        actions.deposit_amount(self.account, self.logger)
        self.assertIn('Error: Deposit amount must be positive.', mock_stdout.getvalue())
        self.assertEqual(self.account.balance, 0)
        self.logger.log.assert_called_with("Deposit amount must be positive.", LogLevel.ERROR)


    @patch('builtins.input', return_value='0')
    @patch('sys.stdout', new_callable=StringIO)
    def test_deposit_zero_shows_error_message(self, mock_stdout, mock_input):
        actions.deposit_amount(self.account, self.logger)
        self.assertIn('Error: Deposit amount must be positive.', mock_stdout.getvalue())
        self.assertEqual(self.account.balance, 0)
        self.logger.log.assert_called_with("Deposit amount must be positive.", LogLevel.ERROR)
        
    @patch('builtins.input', return_value='200')
    @patch('sys.stdout', new_callable=StringIO)
    def test_overdraft_shows_error_message(self, mock_stdout, mock_input):
        self.account.add_amount(100)
        actions.withdraw_amount(self.account, self.logger)
        self.assertIn("Error: Insufficient funds. Overdraft not allowed.", mock_stdout.getvalue())
        self.logger.log.assert_called_with("Insufficient funds. Overdraft not allowed.", LogLevel.ERROR)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_summary(self, mock_stdout):
        self.account.add_amount(150)
        actions.show_summary(self.account, self.logger)
        output = mock_stdout.getvalue()
        self.assertIn("Balance: $150.0, Last Transaction: +150.0", output)
        self.logger.log.assert_called_with("Generated account summary")