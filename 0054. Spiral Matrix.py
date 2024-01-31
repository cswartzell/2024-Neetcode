# 01-31-2024 Neetcode 0054. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Time: 20 minutes first sol, 15 second. Challenge: 3/10

# Right, Down, Left, Up, RIGHT ONE SQUARE. Repeat

# The second method is hinted at in the solutions page and is absolutely asinine
# ... but it does work, and is at least a different way of thinking about it.
# If I had to extend this to 3+ dimensions I'd probably do it the second way
# It's a bit confusing tracking and efficiently manipulating the boundaries. 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # ans = []

        # min_row, min_col = 0, 0
        # max_row, max_col = len(matrix), len(matrix[0])
        
        # while min_row < max_row or min_col < max_col:
        #     #Right:
        #     if min_row < max_row:
        #         for curr_col in range(min_col, max_col):
        #             ans.append(matrix[min_row][curr_col])
        #         min_row += 1
                

        #     #Down 
        #     if min_col < max_col:
        #         for curr_row in range(min_row, max_row):
        #             ans.append(matrix[curr_row][max_col - 1])
        #         max_col -= 1

        #     #Left
        #     if min_row < max_row:
        #         for curr_col in range(max_col - 1, min_col - 1, -1):
        #             ans.append(matrix[max_row - 1][curr_col])
        #         max_row -= 1

        #     #Up
        #     if min_col < max_col:
        #         for curr_row in range(max_row - 1, min_row - 1, -1):
        #             ans.append(matrix[curr_row][min_col])
        #         min_col += 1

        # return ans
    
        m, n = len(matrix), len(matrix[0])

        visited = set(
                   [(-1,x) for x in range(n)] +
                   [(m, x) for x in range(n)] +
                   [(x,-1) for x in range(m)] +
                   [(x, n) for x in range(m)])

        steps = [(0,1), (1,0),(0,-1),(-1,0)]
        curr_step = 0
        row_delta, col_delta = steps[curr_step]

        prev_row, prev_col = 0, -1
        ans = []
        
        while len(ans) < len(matrix) * len(matrix[0]):
            new_row = prev_row + row_delta
            new_col = prev_col + col_delta
            if (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                ans.append(matrix[new_row][new_col])
                prev_row, prev_col = new_row, new_col
            else:
                curr_step = (curr_step + 1) % 4
                row_delta, col_delta = steps[curr_step]

        return ans


