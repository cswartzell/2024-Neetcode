# 02-03-2024 Neetcode 0011. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/submissions/1165635979/
# Time: 15 challenge: 6/10

only solved easily as I've memorized this'

class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        max_water = 0
        while L < R:
            max_water = max(max_water, (R - L) * (min(height[R], height[L])))
            if height[L] < height[R]:
                L += 1
            elif height[R] < height[L]:
                R -= 1
            else:
                L += 1
                R -= 1

        return max_water


