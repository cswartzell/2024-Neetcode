# 02-02-2023 Neetcode 0049. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Time: 5mins Challenge: 2/10
# Only due to some lazy fumbling, trying to hash a set and using the key
# instead of values FROM my dict. Cant be lazy just because the question is easy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for word in strs:
            groups[tuple(sorted(word))].append(word)

        return [groups[group] for group in groups]

