"""A simple command-line calculator."""

import re
from collections.abc import Sequence

from simple_calculator._cli import build_parser


EXPRESSION_PATTERN = re.compile(
    r"\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)"
    r"\s*([+\-*/])\s*"
    r"([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)\s*"
)


def calculate(first: float, operator: str, second: float) -> float:
    """Calculate the result of a basic arithmetic operation."""
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second
    raise ValueError("Unknown operator. Use +, -, *, or /.")


def evaluate_expression(expression: str) -> float:
    """Evaluate a two-number arithmetic expression such as '12 / 3'."""
    match = EXPRESSION_PATTERN.fullmatch(expression)
    if match is None:
        raise ValueError("Enter a valid expression, such as 12 + 3")
    first, operator, second = match.groups()
    return calculate(float(first), operator, float(second))


def main(argv: Sequence[str] | None = None) -> None:
    """Run the interactive command-line calculator."""
    parser = build_parser("A simple command-line calculator.")
    parser.parse_args(argv)

    print("Simple Calculator (enter 'q' to quit)")

    while True:
        try:
            expression = input("Expression (e.g. 2 + 3): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if expression.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        parts = expression.split()
        if len(parts) != 3:
            print("Please enter an expression like: 2 + 3")
            continue

        try:
            first = float(parts[0])
            operator = parts[1]
            second = float(parts[2])
            result = calculate(first, operator, second)
            print(f"= {result:g}")
        except ValueError as error:
            print(f"Invalid input: {error}")
        except ZeroDivisionError as error:
            print(error)


if __name__ == "__main__":
    main()
