# 02-02-2024 Neetcode 0078. Subsets
# https://leetcode.com/problems/subsets/
# Time: 19 minutes Challenge: 3/10 Thoug annoyed about the bit method. Feels cheap,
# as I should be able to build off existing sets rather than building
# each up from scratch, checking EACH bit each time



# Counting in binary and using that as a mask for each digit gets you there
# but it seems monstrously inefficient. I need to extract the bits each time
# rather than building on what we have? There HAS to be a better way.

# I could just do it as sets and check for inclusion, then conver them all to 
# lists later. For each element in the last set, add each element of nums to it,
# and add these to a new set. Add the last set to ans. Doing them as sets means
# we dont have to do checks for duplicates, just add naively. Start wit the empty
# set, add each num to it to get the single digits. For each of those, add each digit
# again to get every combination of two... except we'll get tons of waste here as 
# adding 1 to {4} is the same as adding 4 to {1}... Is it just nested fors starting
# with i = 0 in one and j = i + 1 as the other?

# lets go bitflag?

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        for bitflag in range(2**len(nums)):
            new_subset = []
            for j in range(len(nums)):
                if 2**j & bitflag:
                    new_subset.append(nums[j])
            ans.append(new_subset)

        return ans
