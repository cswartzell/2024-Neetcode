# 01-27-2024 Leetcode 0242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/
# Time: 60 seconds


from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) 
        # return sorted(s) == sorted(t)




