# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Desktop calculator UI using Tkinter.
- Type hints for all public functions.
- Pre-commit hooks for linting and type checking.
- GitHub Actions workflows for CI.
- `--version` flag for CLI and UI entry points.
- `py.typed` marker for type hints.

### Fixed
- Tests no longer require Tkinter, so they pass on headless CI runners.

## [0.1.0] - 2026-11-06

### Added
- Command-line calculator supporting addition, subtraction, multiplication, and division.
- Unit tests for the calculator logic and CLI.
- Pylint for code quality.