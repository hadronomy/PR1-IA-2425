"""Maze data structure."""

from enum import Enum
from typing import TypeVar

from .matrix import Matrix


class MazeTile(str, Enum):
    """Maze tile class."""

    WALL = "#"
    EMPTY = " "
    START = "S"
    GOAL = "G"


class Maze(Matrix):
    """Maze data structure."""

    def __init__(self, *, rows: int, cols: int) -> None:
        super().__init__(rows=rows, cols=cols, default=MazeTile.EMPTY)


TContent = TypeVar("TContent", bound=MazeTile)
