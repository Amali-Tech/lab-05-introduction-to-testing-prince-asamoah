# Python Accelerator Upskilling Lab 05 Project

## Real-World Use Case: Banking Utility Validation

A financial service provider requires a transaction utility that:

· Adds and withdraws amounts from an account

· Prevents overdrafts

· Generates a balance summary

Your task:

· Implement the functionality using TDD principles

· Write unit tests for each function

· Use mocking to simulate an external logging service without calling it directly

This simulates a core feature for client projects where correctness and reliability are critical.


### Sub-Labs / Challenges

#### Sub-Lab 1: Basic Unit Test Setup

· Focus: Create first test cases using unittest

· Task: Write tests for add_amount() and withdraw_amount()

· Expected Outcome: All tests pass for implemented functions

· Test Case: Add 100 → balance = 100

#### Sub-Lab 2: Edge Cases and Assertions

· Focus: Test edge cases like zero, negative values, overdrafts

· Task: Ensure withdrawal does not allow balance < 0

· Expected Outcome: Overdraft attempt raises ValueError

· Test Case: Withdraw 150 from balance 100 → Exception raised


#### Sub-Lab 3: Apply TDD Principles

· Focus: Implement a new generate_summary() function

· Task: Write test first, then implement logic

· Expected Outcome: Summary includes account balance and last transaction

· Test Case: Output string: "Balance: $100, Last Transaction: +100"

#### Sub-Lab 4: Simple Mocking

· Focus: Use unittest.mock to patch a logging function

· Task: Log each transaction without calling real logging service

· Expected Outcome: Tests confirm the mock was called correctly

· Test Case: Assert mock_logger.log called once on deposit


#### Sub-Lab 5: Full Test Suite Execution

· Focus: Combine all tests into a single test suite

· Task: Run suite and ensure all tests pass consistently

· Expected Outcome: Coverage report includes all key paths
