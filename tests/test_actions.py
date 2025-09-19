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
        """Cleanup bank account"""
        del self.account

    @patch("actions.logger")  # patch the global logger in actions.py
    @patch("builtins.input", return_value="100")
    @patch("sys.stdout", new_callable=StringIO)
    def test_deposit_amount(self, mock_stdout, mock_input, mock_logger):
        actions.deposit_amount(self.account)
        mock_input.assert_called_once_with("Enter amount to deposit: ")
        self.assertEqual(self.account.balance, 100)
        self.assertIn("Deposited $100.0.", mock_stdout.getvalue())
        self.assertIn("New Balance: $100.0", mock_stdout.getvalue())
        mock_logger.log.assert_called_with("Deposited $100.0")

    @patch("actions.logger")
    @patch("builtins.input", return_value="50")
    @patch("sys.stdout", new_callable=StringIO)
    def test_withdraw_amount(self, mock_stdout, mock_input, mock_logger):
        self.account.add_amount(100)  # preload balance
        actions.withdraw_amount(self.account)
        mock_input.assert_called_once_with("Enter amount to withdraw: ")
        self.assertEqual(self.account.balance, 50)
        self.assertIn("Withdrawn $50.0.", mock_stdout.getvalue())
        self.assertIn("New Balance: $50.0", mock_stdout.getvalue())
        mock_logger.log.assert_called_with("Withdrew $50.0")

    @patch("actions.logger")
    @patch("builtins.input", return_value="-50")
    @patch("sys.stdout", new_callable=StringIO)
    def test_deposit_negative_shows_error_message(self, mock_stdout, mock_input, mock_logger):
        actions.deposit_amount(self.account)
        self.assertIn("Error: Deposit amount must be positive.", mock_stdout.getvalue())
        self.assertEqual(self.account.balance, 0)
        mock_logger.log.assert_called()

    @patch("actions.logger")
    @patch("builtins.input", return_value="0")
    @patch("sys.stdout", new_callable=StringIO)
    def test_deposit_zero_shows_error_message(self, mock_stdout, mock_input, mock_logger):
        actions.deposit_amount(self.account)
        self.assertIn("Error: Deposit amount must be positive.", mock_stdout.getvalue())
        self.assertEqual(self.account.balance, 0)
        mock_logger.log.assert_called()

    @patch("actions.logger")
    @patch("builtins.input", return_value="200")
    @patch("sys.stdout", new_callable=StringIO)
    def test_overdraft_shows_error_message(self, mock_stdout, mock_input, mock_logger):
        self.account.add_amount(100)
        actions.withdraw_amount(self.account)
        self.assertIn("Error: Insufficient funds. Overdraft not allowed.", mock_stdout.getvalue())
        mock_logger.log.assert_called()

    @patch("actions.logger")
    @patch("sys.stdout", new_callable=StringIO)
    def test_show_summary(self, mock_stdout, mock_logger):
        self.account.add_amount(150)
        actions.show_summary(self.account)
        output = mock_stdout.getvalue()
        self.assertIn("Balance: $150.0, Last Transaction: +150.0", output)
        mock_logger.log.assert_called_with("Generated account summary")
