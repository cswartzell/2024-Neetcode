# 01-24-2024 Neetcode150  Leetcode 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# time: 10 seconds or so

# import typing
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))





tests = [[1,2,3,4,5], [1,1,1,2,3,4],[],[7,6,5,4]]

tester = Solution()

assert tester.containsDuplicate(tests[0]) == False    
assert tester.containsDuplicate(tests[1]) == True
assert tester.containsDuplicate(tests[2]) == False
assert tester.containsDuplicate(tests[3]) == False



# # 09-11-2023 Neetcode 217. Contains Duplicate
# # https://leetcode.com/problems/contains-duplicate/
# # Time: 60 seconds

# # Could make my own counter if I wanted, iterate it manually etc


# # class Solution:
# #     def containsDuplicate(self, nums: List[int]) -> bool:
#         return max(collections.Counter(nums).values()) > 1