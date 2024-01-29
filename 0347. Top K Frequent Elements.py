# 01-28-20234 Neetcode 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Time: 5 mins

# NOTE: QUICKSELECT POSSIBLE HERE. Maybe DONT memorize, but 
# get a feeling for, and maybe mention
# Also possible: Median of Medians

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        return [num[1] for num in sorted([(freq, num) for num, freq in collections.Counter(nums).items()])[-k:]]