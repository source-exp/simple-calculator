"""A simple command-line calculator."""


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


def main() -> None:
    """Run the interactive command-line calculator."""
    print("Simple Calculator (enter 'q' to quit)")

    while True:
        expression = input("Expression (e.g. 2 + 3): ").strip()
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
