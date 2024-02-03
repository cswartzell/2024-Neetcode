# 02-02-2024 Neetcode 0238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Time: 15 mins Challenge: 2/10

# If we could divide you'd just multiply the whole array, then divide
# for each num in the array. EXCEPT this may overflow: we are only guarenteed
# that the prefix * suffix for each index wont overflow, but NOT when then multiplying
# by the value at that index. Moot, division is specifically verbotten.

# The hint is in the description: the product of the prefix and suffix are under 2**32
# Calculate the prefix product array and suffix product array. Step through and multiply
# for both. Lets pad each out by 1 so its easier

# This time I took the extra 5 mins to do it on paper and makes sure I didnt have any
# indexing issues on generating the final array (which is good as I WOULD have if
# I had submitted my first guess). Carefull double checking for small errors like this
# is key. I need to get out of lazily relying on debugging. 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        for i in range(len(nums)):
            prefixes.append(nums[i] * prefixes[-1])

        suffixes = [1]
        for i in range(len(nums) - 1, -1, -1):
            suffixes.append(nums[i] * suffixes[-1])
        suffixes = suffixes[::-1]

        ans = [prefixes[i]*suffixes[i + 1] for i in range(len(nums))]

        return [prefixes[i]*suffixes[i + 1] for i in range(len(nums))]