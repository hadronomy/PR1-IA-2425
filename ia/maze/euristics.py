"""Euristic functions for the A* algorithm."""

import math

from ia.maze.matrix import MatrixPosition


def manhattan_distance(start: MatrixPosition, goal: MatrixPosition) -> int:
    """Calculate the Manhattan distance between two positions.

    The Manhattan distance is the sum of the horizontal and vertical distances
    between two positions. With an adjustment factor of 3.

    Examples
    --------
    >>> start = MatrixPosition(0, 0)
    >>> goal = MatrixPosition(3, 4)
    >>> manhattan_distance(start, goal)
    21

    Parameters
    ----------
        start : MatrixPosition
            The start position.
        goal : MatrixPosition
            The goal position.
    """
    return (abs(start.row - goal.row) + abs(start.col - goal.col)) * 3


def euclidean_distance(start: MatrixPosition, goal: MatrixPosition) -> float:
    """Calculate the Euclidean distance between two positions.

    Examples
    --------
    >>> start = MatrixPosition(0, 0)
    >>> goal = MatrixPosition(3, 4)
    >>> euclidean_distance(start, goal)
    5.0

    Parameters
    ----------
        start : MatrixPosition
            The start position.
        goal : MatrixPosition
            The goal position.
    """
    return math.floor(
        ((start.row - goal.row) ** 2 + (start.col - goal.col) ** 2) ** 0.5
    )


def chebyshev_distance(start: MatrixPosition, goal: MatrixPosition) -> int:
    """Calculate the Chebyshev distance between two positions.

    The Chebyshev distance is the maximum of the horizontal and vertical
    distances between two positions.

    Examples
    --------
    >>> start = MatrixPosition(0, 0)
    >>> goal = MatrixPosition(3, 4)
    >>> chebyshev_distance(start, goal)
    4

    Parameters
    ----------
        start : MatrixPosition
            The start position.
        goal : MatrixPosition
            The goal position.
    """
    return max(abs(start.row - goal.row), abs(start.col - goal.col))


def octile_distance(start: MatrixPosition, goal: MatrixPosition) -> int:
    """Calculate the Octile distance between two positions.

    The Octile distance is the sum of the horizontal and vertical distances
    between two positions plus the diagonal distance.

    Examples
    --------
    >>> start = MatrixPosition(0, 0)
    >>> goal = MatrixPosition(3, 4)
    >>> octile_distance(start, goal)
    5

    Parameters
    ----------
        start : MatrixPosition
            The start position.
        goal : MatrixPosition
            The goal position.
    """
    dx = abs(start.row - goal.row)
    dy = abs(start.col - goal.col)
    return math.floor(dx + dy + (math.sqrt(2) - 2) * min(dx, dy))


def greater_diagonal_g_score(current: MatrixPosition, neighbor: MatrixPosition) -> int:
    """Calculate the greater diagonal g score between two positions.

    The greater diagonal g score is 7 if the neighbor is diagonal to the current
    position and 5 if it is horizontal or vertical.

    Examples
    --------
    >>> current = MatrixPosition(0, 0)
    >>> neighbor = MatrixPosition(1, 1)
    >>> greater_diagonal_g_score(current, neighbor)
    7
    """
    offset = neighbor - current
    if offset == (0, 1) or offset == (1, 0) or offset == (0, -1) or offset == (-1, 0):
        return 5
    return 7
