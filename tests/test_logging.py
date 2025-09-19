import unittest
from io import StringIO
from unittest.mock import patch
from logger import LoggerService, LogLevel

class TestLogging(unittest.TestCase):
    def setUp(self) -> None:
        self.logger = LoggerService(name="TestLogger")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_info_log(self, mock_stdout):
        test_log_message = 'This is an info message'
        self.logger.log(test_log_message, level=LogLevel.INFO)
        output = mock_stdout.getvalue().strip()
        self.assertIn("[TestLogger]", output)
        self.assertIn("[INFO]", output)
        self.assertIn(test_log_message, output)
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_error_log(self, mock_stdout):
        test_log_message = 'This is an error message'
        self.logger.log(test_log_message, level=LogLevel.ERROR)
        output = mock_stdout.getvalue().strip()
        self.assertIn("[TestLogger]", output)
        self.assertIn("[ERROR]", output)
        self.assertIn(test_log_message, output)
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_debug_log(self, mock_stdout):
        test_log_message = 'This is a debug message'
        self.logger.log(test_log_message, level=LogLevel.DEBUG)
        output = mock_stdout.getvalue().strip()
        self.assertIn("[TestLogger]", output)
        self.assertIn("[DEBUG]", output)
        self.assertIn(test_log_message, output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_warning_log(self, mock_stdout):
        test_log_message = 'This is a warning message'
        self.logger.log(test_log_message, level=LogLevel.WARNING)
        output = mock_stdout.getvalue().strip()
        self.assertIn("[TestLogger]", output)
        self.assertIn("[WARNING]", output)
        self.assertIn(test_log_message, output)
    