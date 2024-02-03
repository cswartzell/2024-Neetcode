# 02-02-2024 Neetcode 0001. Two Sum
# https://leetcode.com/problems/two-sum/
# Time: 2 mins Challenges: 1/10


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            if target - num in seen:
                return [idx, seen[target-num]]
            else:
                seen[num] = idx 

        return []





# 09-11-2023 Neetcode 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Time: 10 minutes for advanced version

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # x_at_i = {val:idx for idx, val in enumerate(nums)}
#         # for i in range(len(nums)):
#         #     if target - nums[i] in x_at_i:
#         #         return [i, x_at_i[target - nums[i]]]
#         val_at_i = collections.defaultdict(int)
#         for idx, num in enumerate(nums):
#             if target - num in val_at_i:
#                 return [idx, val_at_i[target - num]]
#             val_at_i[num] = idx