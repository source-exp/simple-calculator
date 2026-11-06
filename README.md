# Simple Calculator

A lightweight calculator written in Python. It supports addition, subtraction,
multiplication, and division, with both command-line and desktop interfaces.

## Requirements

- Python 3.10 or newer
- [uv](https://docs.astral.sh/uv/)
- Tkinter for the desktop interface (use a Python installation that includes
  it; uv-managed Python builds may not)

## Setup

Install the project and its development tools:

```sh
uv sync
```

## Run

Start the command-line calculator with:

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
and Escape to clear.

Both interfaces accept `--version`:

```sh
uv run simple-calculator --version
uv run simple-calculator-ui --version
```

You can also run the command-line interface without installing the project:

```sh
uv run python -m simple_calculator.calculator
```

## Project structure

```text
.
├── src/simple_calculator/
│   ├── __init__.py
│   ├── _cli.py          # Shared argument parsing
│   ├── calculator.py    # Arithmetic logic and CLI
│   ├── calculator_ui.py # Tkinter desktop interface
│   ├── version.py       # Package version
│   └── py.typed         # Marks the package as typed
├── tests/
│   └── test_calculator.py
├── pyproject.toml
└── README.md
```

## Tests and linting

Run the unit tests:

```sh
uv run python -m unittest discover -v
```

Run Pylint and mypy:

```sh
uv run pylint src/simple_calculator tests
uv run mypy
```

Build source and wheel distributions with:

```sh
uv build
```

## Pre-commit hooks

Install the hooks once to lint and type-check changed files before each commit:

```sh
uv run pre-commit install
```

Run all hooks manually with:

```sh
uv run pre-commit run --all-files
```

## Continuous integration

The GitHub Actions workflow in `.github/workflows/ci.yml` runs the tests,
Pylint, mypy, and a package build on every push and pull request.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history.
