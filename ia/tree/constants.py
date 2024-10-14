"""Tree related constants."""

from collections.abc import Iterator
from dataclasses import dataclass


class ExportConstants:  # noqa: D101
    """Constants for representing the tree as a string."""

    DOWN_RIGHT = "\u250c"
    VERTICAL_RIGHT = "\u251c"
    VERTICAL_LEFT = "\u2524"
    VERTICAL_HORIZONTAL = "\u253c"
    UP_RIGHT = "\u2514"
    VERTICAL = "\u2502"
    HORIZONTAL = "\u2500"

    DOWN_RIGHT_ROUNDED = "\u256d"
    UP_RIGHT_ROUNDED = "\u2570"

    DOWN_RIGHT_BOLD = "\u250f"
    VERTICAL_RIGHT_BOLD = "\u2523"
    VERTICAL_LEFT_BOLD = "\u252b"
    VERTICAL_HORIZONTAL_BOLD = "\u254b"
    UP_RIGHT_BOLD = "\u2517"
    VERTICAL_BOLD = "\u2503"
    HORIZONTAL_BOLD = "\u2501"

    DOWN_RIGHT_DOUBLE = "\u2554"
    VERTICAL_RIGHT_DOUBLE = "\u2560"
    VERTICAL_LEFT_DOUBLE = "\u2563"
    VERTICAL_HORIZONTAL_DOUBLE = "\u256c"
    UP_RIGHT_DOUBLE = "\u255a"
    VERTICAL_DOUBLE = "\u2551"
    HORIZONTAL_DOUBLE = "\u2550"

    PRINT_STYLES: dict[str, tuple[str, str, str]] = {
        "ansi": ("|   ", "|-- ", "`-- "),
        "ascii": ("|   ", "|-- ", "+-- "),
        "const": (
            f"{VERTICAL}   ",
            f"{VERTICAL_RIGHT}{HORIZONTAL}{HORIZONTAL} ",
            f"{UP_RIGHT}{HORIZONTAL}{HORIZONTAL} ",
        ),
        "const_bold": (
            f"{VERTICAL_BOLD}   ",
            f"{VERTICAL_RIGHT_BOLD}{HORIZONTAL_BOLD}{HORIZONTAL_BOLD} ",
            f"{UP_RIGHT_BOLD}{HORIZONTAL_BOLD}{HORIZONTAL_BOLD} ",
        ),
        "rounded": (
            f"{VERTICAL}   ",
            f"{VERTICAL_RIGHT}{HORIZONTAL}{HORIZONTAL} ",
            f"{UP_RIGHT_ROUNDED}{HORIZONTAL}{HORIZONTAL} ",
        ),
        "double": (
            f"{VERTICAL_DOUBLE}   ",
            f"{VERTICAL_RIGHT_DOUBLE}{HORIZONTAL_DOUBLE}{HORIZONTAL_DOUBLE} ",
            f"{UP_RIGHT_DOUBLE}{HORIZONTAL_DOUBLE}{HORIZONTAL_DOUBLE} ",
        ),
    }

    HPRINT_STYLES: dict[str, tuple[str, str, str, str, str, str, str]] = {
        "ansi": ("/", "+", "+", "+", "\\", "|", "-"),
        "ascii": ("+", "+", "+", "+", "+", "|", "-"),
        "const": (
            DOWN_RIGHT,
            VERTICAL_RIGHT,
            VERTICAL_LEFT,
            VERTICAL_HORIZONTAL,
            UP_RIGHT,
            VERTICAL,
            HORIZONTAL,
        ),
        "const_bold": (
            DOWN_RIGHT_BOLD,
            VERTICAL_RIGHT_BOLD,
            VERTICAL_LEFT_BOLD,
            VERTICAL_HORIZONTAL_BOLD,
            UP_RIGHT_BOLD,
            VERTICAL_BOLD,
            HORIZONTAL_BOLD,
        ),
        "rounded": (
            DOWN_RIGHT_ROUNDED,
            VERTICAL_RIGHT,
            VERTICAL_LEFT,
            VERTICAL_HORIZONTAL,
            UP_RIGHT_ROUNDED,
            VERTICAL,
            HORIZONTAL,
        ),
        "double": (
            DOWN_RIGHT_DOUBLE,
            VERTICAL_RIGHT_DOUBLE,
            VERTICAL_LEFT_DOUBLE,
            VERTICAL_HORIZONTAL_DOUBLE,
            UP_RIGHT_DOUBLE,
            VERTICAL_DOUBLE,
            HORIZONTAL_DOUBLE,
        ),
    }


@dataclass
class BasePrintStyle:
    """Base style for `print_tree` and `yield_tree`."""

    stem: str
    branch: str
    strem_final: str

    def __iter__(self) -> Iterator[str]:
        """Iterate over attributes."""
        return iter([self.stem, self.branch, self.strem_final])

    def __post_init__(self) -> None:
        """Post initialization."""
        if not len(self.stem) == len(self.branch) == len(self.strem_final):
            raise ValueError("All attributes must be of same length.")
