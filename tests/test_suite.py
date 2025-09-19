import unittest

from tests.test_banking import TestBankAcount
from tests.test_actions import TestActions
from tests.test_logging import TestLogging

def suite():
    """Aggregate all test cases into one suite."""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    
    # Add test classes explicitly
    suite.addTests(loader.loadTestsFromTestCase(TestBankAcount))
    suite.addTest(loader.loadTestsFromTestCase(TestActions))
    suite.addTest(loader.loadTestsFromTestCase(TestLogging))
    
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())