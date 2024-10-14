"""Constants for the maze module."""

from ia.maze.tile import MazeTile

ALPHABET = [chr(letter) for letter in range(65, 91)]
"""A list with the uppercase alphabet letters."""

NUMBERS = [str(number) for number in range(0, 10)]
"""A list with the numbers from 0 to 9."""

MAZE_PRINT_STYLES = {
    MazeTile.WALL: "■",
    MazeTile.EMPTY: " ",
    MazeTile.START: "S",
    MazeTile.GOAL: "G",
    "path": "*",
}
"""A dictionary with the styles for printing the maze.

Each key is a MazeTile or the string "path" and its value is the character to
use when printing the maze.
"""

DEFAULT_MAZE_MAPPINGS = {
    "0": MazeTile.EMPTY,
    "1": MazeTile.WALL,
    "3": MazeTile.START,
    "4": MazeTile.GOAL,
}
"""A dictionary with the default mappings for the maze.

Each key is a string and its value is a MazeTile. The keys are the values that
can be found in the maze file and the values are the MazeTile that they
represent.
"""
