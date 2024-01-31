# 01-30-2024 Neetcode 0048. Rotate Image
# https://leetcode.com/problems/rotate-image/
# time: 25  challenge: 6/10

# Iterating in kind of a spiral is easy, just took a minute
# to get clear in my head how a nested row/col loop affected
# the 4 cells we were looking at, then how to make sure we only
# touch each cell once (spiraling in). Kind of a neat problem.
# My code is one line ugly. I should perhaps make named tuple assignments
# per the comments, then do the actual swaps using the assigned names so
# its more clear what is going on. That, or use a temp variable and assign
# them one by one in a spiral, each on a seperate line, 5 times (for tmp)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) - 1         # row nums
        n = len(matrix[0]) - 1      # col nums

        for row in range(m//2 + 1):
            for col in range(row, n - row):
                # top_leftT  = (row, col)
                # top_rightT = (col, n - row)
                # bot_rightT = (m-row, n - col)
                # bot_leftT  = (m - col, row)

                # top_left  = matrix[row][col]
                # top_right = matrix[col][n - row]
                # bot_right = matrix[m - row][n - col]
                # bot_left  = matrix[m - col][row]
        
                matrix[col][n - row], matrix[m - row][n - col],  matrix[m - col][row], matrix[row][col] = matrix[row][col], matrix[col][n - row], matrix[m - row][n - col], matrix[m - col][row]
        
        pass
