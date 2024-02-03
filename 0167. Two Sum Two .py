# 02-02-2024 Neetcode 0167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Time: 2mins Challnege 2/10- somewhat harder to do the binary seach method


# If we can only use contant space, can we do better than O(n**2)?
# Two pointer is trivial. Binary search is doable.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] > target:
                R -= 1
            elif numbers[L] + numbers[R] < target:
                L += 1
            else:
                return [L+1, R+1]

        return []
