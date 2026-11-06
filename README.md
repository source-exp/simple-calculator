# Simple Calculator

A lightweight command-line calculator written in Python. It supports addition,
subtraction, multiplication, and division, with both command-line and desktop
interfaces.

## Requirements

- Python 3.10 or newer
- [uv](https://docs.astral.sh/uv/)

## Setup

Install the project and its development tools:

```sh
uv sync
```

## Run

Start the calculator with:

```sh
uv run simple-calculator
```

Enter an expression with spaces around the operator, such as `12 / 3`. Enter
`q`, `quit`, or `exit` to close the calculator.

To launch the desktop calculator, run:

```sh
uv run simple-calculator-ui
```

The desktop interface also accepts keyboard input; press Enter to calculate
and Escape to clear. It requires a Python installation that includes Tkinter.

You can also run it without installing the project:

```sh
uv run python calculator.py
```

## Tests and linting

Run the unit tests:

```sh
uv run python -m unittest -v
```

Run Pylint:

```sh
uv run pylint calculator.py test_calculator.py
```
