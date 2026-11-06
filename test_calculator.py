"""Tests for the simple command-line calculator."""

import unittest
from unittest.mock import patch

from calculator import calculate, main
from calculator_ui import evaluate_expression


class CalculateTests(unittest.TestCase):
    """Tests for the calculate function."""

    def test_addition(self):
        """Return the sum of two numbers."""
        self.assertEqual(calculate(2, "+", 3), 5)

    def test_subtraction(self):
        """Return the difference of two numbers."""
        self.assertEqual(calculate(7, "-", 4), 3)

    def test_multiplication(self):
        """Return the product of two numbers."""
        self.assertEqual(calculate(3, "*", 4), 12)

    def test_division(self):
        """Return the quotient of two numbers."""
        self.assertEqual(calculate(8, "/", 2), 4)

    def test_division_by_zero(self):
        """Reject division by zero."""
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero"):
            calculate(1, "/", 0)

    def test_unknown_operator(self):
        """Reject unsupported arithmetic operators."""
        with self.assertRaisesRegex(ValueError, "Unknown operator"):
            calculate(1, "%", 2)


class ExpressionTests(unittest.TestCase):
    """Tests for expressions entered in the graphical calculator."""

    def test_evaluates_expression_without_spaces(self):
        """Accept an expression without whitespace around its operator."""
        self.assertEqual(evaluate_expression("12/3"), 4)

    def test_evaluates_negative_number(self):
        """Handle a signed second operand."""
        self.assertEqual(evaluate_expression("2 * -3"), -6)

    def test_rejects_malformed_expression(self):
        """Reject expressions containing more than one operation."""
        with self.assertRaisesRegex(ValueError, "valid expression"):
            evaluate_expression("2 + 3 + 4")

    def test_division_by_zero(self):
        """Propagate division-by-zero errors from the shared calculator."""
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero"):
            evaluate_expression("1 / 0")


class MainTests(unittest.TestCase):
    """Tests for the interactive command-line interface."""

    @patch("builtins.input", side_effect=["2 + 3", "q"])
    def test_main_calculates_and_quits(self, _mock_input):
        """Print a calculation result and exit on the quit command."""
        with patch("builtins.print") as mock_print:
            main()

        mock_print.assert_any_call("= 5")
        mock_print.assert_any_call("Goodbye!")

    @patch("builtins.input", side_effect=["2 +", "q"])
    def test_main_rejects_malformed_expression(self, _mock_input):
        """Prompt again when the expression has the wrong format."""
        with patch("builtins.print") as mock_print:
            main()

        mock_print.assert_any_call("Please enter an expression like: 2 + 3")


if __name__ == "__main__":
    unittest.main()
