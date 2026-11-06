# Simple Calculator

A lightweight command-line calculator written in Python. It supports addition,
subtraction, multiplication, and division.

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
