# 01-31-2024 Neetcode 0202. Happy Number
# https://leetcode.com/problems/happy-number/
# Time: Challenge:

# This seems both simple and not. The algorithm is simple:
# sum the squares of the digits of a number til it equals 1...
# or loops (or spirals out infinitely?) Theres the rub. I dont know how
# to prove this wont run forever. For looping, we can of course keep track
# of nums we've seen. But what about the spiraling issue? Can we prove mathematically
# this is a non-issue?

# (9)**2 = 81 -> 8**2 + 1**2 = 65 -> 6**2 + 5**2 = 61 -> 6**2 + 1**2 = 37 -> 3**2 + 7**2 = 58
# -> 5**2 + 8**2 = 89. Well we have a 9 in our new number but have GAINED an 8. That means regardless
# of what happens witht that 8 we will just keep collecting digits and grow infinitely.breakpoint

# Well damn. I'm not sure I can say with confidence any given number doesnt just increase without end.

# Wait... this is a trick. If we are summing the digits and adding them together, the only way for them
# to equal 1 is if the digits consisted of a single 1, and ANY number of zeros. Thats it. Any other integers
# will be positive. So the question is if THEIR square sums can become 1 followed by x many zeros. Is there
# a way to know this?

# I'm missing something if this is an EASY. 

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr_num = n
        while curr_num != 1:
            if curr_num in seen:
                return False
            seen.add(curr_num)
            curr_num = sum(int(x)**2 for x in str(curr_num))
        return True