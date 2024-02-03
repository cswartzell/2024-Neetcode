# 02-02-2024 Neetcode 0015. 3Sum
# https://leetcode.com/problems/3sum/
# Time: Challenge:

# We can obviously do O(n**3) in 3 nested fors...
# but there was some trick to get it to O(n**2)
# We COULD collect a dict of {num:[indexes, ]}
# and do an O(n**2) for i, j then add each index from the list of remaining
# such that it is larger than j... dont love it. binary search THAT?
# Thatd be O(n**2 * log(n))


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counted_nums = collections.defaultdict(int)
        for num in nums:
            counted_nums[num] += 1

        ans = []

        # Check triple zero case:
        # UGH. If you just check counted_nums[0] >= 3 as part of a default dict it ADDS 0:0 to the dict
        # if it didnt exist in it. We need to check its inclusion BEFORE count to avoid this. 
        if 0 in counted_nums and counted_nums[0] >= 3:
            ans.append([0,0,0])

        # Now we can limit all occurences of nums to just 2
        # as you cant have 3 copies of the same num sum to zero other than 0,0,0
        # For the same reason, we can limit the number of copies of 0 to just one.

        if 0 in counted_nums:
            counted_nums[0] = 1
        num_keys = sorted(counted_nums.keys())
        new_nums = []

        for num in num_keys:
            new_nums.append(num)
            if counted_nums[num] > 1:
                new_nums.append(num)


        for j in range(1, len(new_nums) - 1):
            i, k = 0, len(new_nums) - 1
            while i < j and j < k:
                new_sum = new_nums[i] + new_nums[j] + new_nums[k]
                if new_sum < 0:
                    i += 1
                elif new_sum > 0:
                    k -= 1
                elif new_sum == 0:
                    if ans == [] or ans[-1] != [new_nums[i], new_nums[j], new_nums[k]]:
                        ans.append([new_nums[i], new_nums[j], new_nums[k]])
                    i += 1
        
        return ans

