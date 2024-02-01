# 02-01-2024 Leetcode 846. Hand of Straights
# https://leetcode.com/problems/hand-of-straights/
# Time: Challenge:


# Wow, this is exactly the same problem I just did.
# Check if divisible by group size.
# Sort and divide. Check each subgroup

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        if groupSize == 1:
            return True

        hand_count = collections.Counter(hand)
        sorted_keys = sorted(hand_count.keys())
        start_idx = 0
        cards = len(hand)

        while cards > 0:
            while hand_count[sorted_keys[start_idx]] == 0:
                start_idx += 1
            group_start = sorted_keys[start_idx]
            
            for next_card in range(group_start + 1, group_start + groupSize):
                if hand_count[next_card] < hand_count[group_start]:
                    return False
                hand_count[next_card] -= hand_count[group_start]

            cards -= groupSize * hand_count[group_start]
            hand_count[group_start] = 0

        return True


        # if len(hand) % groupSize != 0:
        #     return False
        
        # if groupSize == 1:
        #     return True

        # hand_count = collections.Counter(hand)

        # while hand_count:
        #     group_start = min(hand_count.keys())
        #     hand_count[group_start] -= 1
        #     if hand_count[group_start] == 0:
        #         del hand_count[group_start]

        #     for next_card in range(group_start + 1, group_start + groupSize):
        #         if next_card not in hand_count:
        #             return False
        #         hand_count[next_card] -= 1
        #         if hand_count[next_card] == 0:
        #             del hand_count[next_card]
        
        # return True
