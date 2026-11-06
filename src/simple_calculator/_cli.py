"""Shared command-line argument handling."""

import argparse

from simple_calculator.version import __version__


def build_parser(description: str) -> argparse.ArgumentParser:
    """Create an argument parser with the standard version option."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser
