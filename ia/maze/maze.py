"""Maze data structure."""

from enum import Enum
from typing import TypeVar

from .matrix import Matrix


class MazeTile(str, Enum):
    """Maze tile class."""

    WALL = "wall"
    EMPTY = "empty"
    START = "start"
    GOAL = "goal"


MAZE_PRINT_STYLES = {
    MazeTile.WALL: "██",
    MazeTile.EMPTY: "  ",
    MazeTile.START: "SS",
    MazeTile.GOAL: "GG",
}


class Maze(Matrix):
    """Maze data structure."""

    def __init__(self, *, rows: int, cols: int) -> None:
        super().__init__(rows=rows, cols=cols, default=MazeTile.WALL)

    def print(self) -> str:
        """Print the maze as a string."""
        top_border = "╭" + "─" * self.cols * 2 + "╮"
        bottom_border = "╰" + "─" * self.cols * 2 + "╯"
        maze_rows = "\n".join(
            "│" + "".join(MAZE_PRINT_STYLES[cell] for cell in row) + "│" for row in self
        )
        return f"{top_border}\n{maze_rows}\n{bottom_border}"

    def __str__(self) -> str:
        """Return the maze as a string."""
        return self.print()


TContent = TypeVar("TContent", bound=MazeTile)
