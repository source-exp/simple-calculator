"""Tkinter graphical interface for the simple calculator."""

import re
import tkinter as tk
from collections.abc import Sequence
from tkinter import ttk

from simple_calculator._cli import build_parser
from simple_calculator.calculator import calculate


EXPRESSION_PATTERN = re.compile(
    r"\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)"
    r"\s*([+\-*/])\s*"
    r"([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)\s*"
)


def evaluate_expression(expression: str) -> float:
    """Evaluate a two-number arithmetic expression from the display."""
    match = EXPRESSION_PATTERN.fullmatch(expression)
    if match is None:
        raise ValueError("Enter a valid expression, such as 12 + 3")
    first, operator, second = match.groups()
    return calculate(float(first), operator, float(second))


class CalculatorWindow:  # pylint: disable=too-few-public-methods
    """Build and manage the calculator window."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Simple Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg="#10131a")

        self.expression = tk.StringVar()
        self.status = tk.StringVar(value="Ready")

        self._configure_style()
        self._build_window()
        self.root.bind("<Return>", lambda _event: self._evaluate())
        self.root.bind("<Escape>", lambda _event: self._clear())

    def _configure_style(self) -> None:
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure(
            "Calculator.TButton",
            font=("Helvetica Neue", 18),
            foreground="#f1f3f8",
            background="#242a36",
            borderwidth=0,
            padding=(8, 13),
        )
        style.map("Calculator.TButton", background=[("active", "#343c4c")])
        style.configure(
            "Operator.TButton",
            font=("Helvetica Neue", 18),
            foreground="#8fa8ff",
            background="#20283a",
            borderwidth=0,
            padding=(8, 13),
        )
        style.map("Operator.TButton", background=[("active", "#303b55")])
        style.configure(
            "Accent.TButton",
            font=("Helvetica Neue", 18, "bold"),
            foreground="#10131a",
            background="#a8f0c6",
            borderwidth=0,
            padding=(8, 13),
        )
        style.map("Accent.TButton", background=[("active", "#c1f8d6")])

    def _build_window(self) -> None:
        frame = tk.Frame(self.root, bg="#10131a", padx=20, pady=20)
        frame.grid(row=0, column=0)

        tk.Label(
            frame,
            text="CALCULATOR",
            bg="#10131a",
            fg="#8790a3",
            font=("Helvetica Neue", 10, "bold"),
            anchor="w",
        ).grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 12))

        self.display = tk.Entry(
            frame,
            textvariable=self.expression,
            justify="right",
            relief="flat",
            bg="#191e28",
            fg="#f1f3f8",
            insertbackground="#a8f0c6",
            font=("Helvetica Neue", 28),
            width=15,
            border=0,
        )
        self.display.grid(row=1, column=0, columnspan=4, sticky="ew", ipady=15)
        self.display.bind("<KeyRelease>", self._reset_status)

        tk.Label(
            frame,
            textvariable=self.status,
            bg="#10131a",
            fg="#a8f0c6",
            font=("Helvetica Neue", 11),
            anchor="e",
            width=27,
        ).grid(row=2, column=0, columnspan=4, sticky="ew", pady=(9, 14))

        keys = [
            ("C", 3, 0, "Operator.TButton", self._clear),
            ("⌫", 3, 1, "Operator.TButton", self._backspace),
            ("÷", 3, 2, "Operator.TButton", lambda: self._insert("/")),
            ("×", 3, 3, "Operator.TButton", lambda: self._insert("*")),
            ("7", 4, 0, "Calculator.TButton", lambda: self._insert("7")),
            ("8", 4, 1, "Calculator.TButton", lambda: self._insert("8")),
            ("9", 4, 2, "Calculator.TButton", lambda: self._insert("9")),
            ("−", 4, 3, "Operator.TButton", lambda: self._insert("-")),
            ("4", 5, 0, "Calculator.TButton", lambda: self._insert("4")),
            ("5", 5, 1, "Calculator.TButton", lambda: self._insert("5")),
            ("6", 5, 2, "Calculator.TButton", lambda: self._insert("6")),
            ("+", 5, 3, "Operator.TButton", lambda: self._insert("+")),
            ("1", 6, 0, "Calculator.TButton", lambda: self._insert("1")),
            ("2", 6, 1, "Calculator.TButton", lambda: self._insert("2")),
            ("3", 6, 2, "Calculator.TButton", lambda: self._insert("3")),
            ("0", 7, 0, "Calculator.TButton", lambda: self._insert("0")),
            (".", 7, 1, "Calculator.TButton", lambda: self._insert(".")),
            ("=", 7, 2, "Accent.TButton", self._evaluate),
        ]

        for key in keys:
            label, row, column, style, command = key
            button = ttk.Button(frame, text=label, style=style, command=command)
            columnspan = 2 if label == "=" else 1
            button.grid(
                row=row,
                column=column,
                columnspan=columnspan,
                sticky="nsew",
                padx=4,
                pady=4,
            )

        for column in range(4):
            frame.grid_columnconfigure(column, weight=1, uniform="keys")

    def _insert(self, value: str) -> None:
        self.display.insert(tk.INSERT, value)
        self.display.focus_set()
        self.status.set("Ready")

    def _clear(self) -> None:
        self.expression.set("")
        self.status.set("Ready")
        self.display.focus_set()

    def _backspace(self) -> None:
        position = self.display.index(tk.INSERT)
        if position > 0:
            self.display.delete(position - 1)
        self.display.focus_set()
        self.status.set("Ready")

    def _reset_status(self, _event: tk.Event) -> None:
        self.status.set("Ready")

    def _evaluate(self) -> None:
        try:
            result = evaluate_expression(self.expression.get())
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            self.status.set(str(error))
            return
        self.status.set(f"= {result:g}")


def main(argv: Sequence[str] | None = None) -> None:
    """Launch the graphical calculator."""
    parser = build_parser("A simple desktop calculator.")
    parser.parse_args(argv)

    root = tk.Tk()
    CalculatorWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
