"""Euristic functions for the A* algorithm."""

import math

from ia.maze.matrix import MatrixPosition


def manhattan_distance(start: MatrixPosition, goal: MatrixPosition) -> int:
    """Calculate the Manhattan distance between two positions."""
    return (abs(start.row - goal.row) + abs(start.col - goal.col)) * 3


def euclidean_distance(start: MatrixPosition, goal: MatrixPosition) -> float:
    """Calculate the Euclidean distance between two positions."""
    return math.floor(
        ((start.row - goal.row) ** 2 + (start.col - goal.col) ** 2) ** 0.5
    )


def chebyshev_distance(start: MatrixPosition, goal: MatrixPosition) -> int:
    """Calculate the Chebyshev distance between two positions."""
    return max(abs(start.row - goal.row), abs(start.col - goal.col))


def octile_distance(start: MatrixPosition, goal: MatrixPosition) -> int:
    """Calculate the Octile distance between two positions."""
    dx = abs(start.row - goal.row)
    dy = abs(start.col - goal.col)
    return math.floor(dx + dy + (math.sqrt(2) - 2) * min(dx, dy))


def greater_diagonal_g_score(current: MatrixPosition, neighbor: MatrixPosition) -> int:
    """Calculate the greater diagonal g score between two positions."""
    offset = neighbor - current
    if offset == (0, 1) or offset == (1, 0) or offset == (0, -1) or offset == (-1, 0):
        return 5
    return 7
