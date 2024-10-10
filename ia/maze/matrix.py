"""Module with matrix data structure."""

from __future__ import annotations

from typing import TypeVar


class MatrixPosition(tuple[int, int]):
    """Matrix position data structure."""

    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    def __str__(self) -> str:
        """Return the position as a string."""
        return f"({self.row}, {self.col})"

    def __repr__(self) -> str:
        """Return the position as a string."""
        return str(self)


class Matrix:
    """Matrix data structure."""

    def __init__(self, *, rows: int, cols: int, default: TContent) -> None:
        self.__rows = rows
        self.__cols = cols
        self.__default = default
        self.__data = [[default for _ in range(cols)] for _ in range(rows)]

    @property
    def rows(self) -> int:
        """Get the number of rows."""
        return self.__rows

    @property
    def cols(self) -> int:
        """Get the number of columns."""
        return self.__cols

    @property
    def default(self) -> TContent:
        """Get the default value."""
        return self.__default

    def adjacent(
        self, row: int, col: int, offsets: list[MatrixPosition] = None
    ) -> dict[MatrixPosition, MatrixPosition]:
        """Get the adjacent cells.

        Parameters
        ----------
            row : (int)
                The row of the cell.
            col : (int)
                The column of the cell.
            offsets : (list[MatrixPosition])
                The offsets to check.
                By default, it checks the 4 cardinal directions and the 4 diagonals.

        Returns
        -------
            (dict[MatrixPosition, MatrixPosition])
                Dictionary with the adjacent cells, where the key is the offset
                and the value is the position.
        """
        if offsets is None:
            offsets = [
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0),
                (1, 1),
                (1, -1),
                (-1, 1),
                (-1, -1),
            ]
        adjacent: dict[MatrixPosition, MatrixPosition] = {}
        for row_offset, col_offset in offsets:
            new_row, new_col = row + row_offset, col + col_offset
            if 0 <= new_row < self.__rows and 0 <= new_col < self.__cols:
                adjacent.update({(row_offset, col_offset): (new_row, new_col)})
        return adjacent

    def is_valid(self, row: int, col: int) -> bool:
        """Check if the position is valid.

        Parameters
        ----------
            row : (int)
                The row of the cell.
            col : (int)
                The column of the cell.

        Returns
        -------
            (bool)
                True if the position is valid, False otherwise.
        """
        return 0 <= row < self.__rows and 0 <= col < self.__cols

    def is_valid_position(self, position: MatrixPosition) -> bool:
        """Check if the position is valid.

        Parameters
        ----------
            position : (MatrixPosition)
                The position to check.

        Returns
        -------
            (bool)
                True if the position is valid, False otherwise.
        """
        return self.is_valid(position[0], position[1])

    def __len__(self) -> int:
        """Return the number of elements in the matrix."""
        return self.__rows * self.__cols

    def __getitem__(self, key: MatrixPosition) -> TContent:
        """Get the value of the matrix."""
        return self.__data[key[0]][key[1]]

    def __setitem__(self, key: MatrixPosition, value: TContent) -> None:
        """Set the value of the matrix."""
        self.__data[key[0]][key[1]] = value

    def __contains__(self, item: TContent) -> bool:
        """Check if the matrix contains the item."""
        return item in self.__data

    def __iter__(self):
        """Iterate over the matrix."""
        yield from self.__data

    def __str__(self) -> str:
        """Return the matrix as a string."""
        horizontal_border = "+" + "-" * (self.__cols * 3 + (self.__cols - 1)) + "+"
        rows_str = "\n".join(
            "| " + " ".join(f"{item:2}" for item in row) + " |" for row in self.__data
        )
        return f"{horizontal_border}\n{rows_str}\n{horizontal_border}"

    def __repr__(self) -> str:
        """Return the matrix as a string."""
        return str(self)


TContent = TypeVar("TContent", bound=any)
