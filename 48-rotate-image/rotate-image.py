from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            # Iterate through the elements of the current outer layer
            for i in range(r - l):
                top, bottom = l, r

                # Save top-left element
                topLeft = matrix[top][l + i]

                # Move bottom-left into top-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom-right into bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top-right into bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move saved top-left into top-right
                matrix[top + i][r] = topLeft

            # Shrink layer bounds toward center
            r -= 1
            l += 1      