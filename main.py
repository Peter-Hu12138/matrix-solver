"""

"""
from pprint import pprint
from typing import Self


class Matrix:
    """
    Representation of matrix

    Representation Invariants:
    - all([len(row) == len(row[0]) for row in rows])
    """
    rows: list[list[float]]

    def __init__(self, rows: list[list[float]]):
        self.rows = rows

    def scale(self, rows: list[list[float]], row: int, scalar: float) -> None:
        """
        Elementary row operations. Scale row in rows by scalar
        """
        rows[row] = [scalar * entry for entry in rows[row]]

    def add_multiple_to(self, rows: list[list[float]], to_row: int, scalar: float, from_row: int):
        """
        Elementary row operations. Add multiple of from_row by scalar to to_row
        """
        rows[to_row] = [
            rows[to_row][index] + scalar * rows[from_row][index]
            for index in range(0, len(rows[0]))
        ]

    def rank(self) -> int:
        """
        Return the rank of the matrix, dim of the range
        """

    def RREF(self) -> list[list[float]]:
        """
        RREF form of rows
        >>> mat = Matrix([[3, 1, 2], [2, 1, 3]])
        >>> mat.RREF() == [[1,0,-1],[0,1,5]]
        True
        """
        rows = self.rows.copy()
        for i in range(0, len(rows)):
            # Step 1: swap 0 rows to bottom
            for row_index in range(0, len(rows)):
                if all([entry == 0 for entry in rows[row_index]]):  # check if all 0's
                    rows.append(rows.pop(row_index))

            # Step 2: Move pivots.
            rank_by_pivot = []
            for col_index in range(0, len(rows[0])):
                row_index = 0
                while row_index < len(rows):
                    if rows[row_index][col_index] != 0:
                        rank_by_pivot.append(rows.pop(row_index))
                        row_index -= 1
                    row_index += 1
            rank_by_pivot += rows
            rows = rank_by_pivot

            # Step 3: Make all pivots equal to 1. +
            # Step 4: Remove nonzero nonpivot entries from pivot columns.
            for row_index in range(0, len(rows)):
                pivot_index = -1
                for index in range(0, len(rows[0])):
                    if rows[row_index][index] != 0:
                        pivot_index = index
                        break
                if pivot_index == -1:
                    break
                self.scale(rows, row_index, 1 / rows[row_index][pivot_index])
                for index in range(0, row_index):
                    self.add_multiple_to(rows, index, -rows[index][pivot_index]/rows[row_index][pivot_index], row_index)

        return rows

    def det(self):
        pass

    def if_dependent(self) -> bool:
        pass

    def if_row_equivalent_to(self, b: Self) -> bool:
        pass


if __name__ == '__main__':
    a = 'sdf'
    a.upper()
