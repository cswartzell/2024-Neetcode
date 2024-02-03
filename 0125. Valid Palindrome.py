# 02-02-2024 Neetcode 0125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Time: 4m Challenge: 1/10

# READ the whole problem. I removed all non-alpha characters but
# the prompt clearly states alpha-NUMERIC is allowed

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (STR:= [str.capitalize(char) for char in s if char in string.ascii_letters + string.digits]) == STR[::-1]



# class Solution:
#     def isPalindrome(self, s: str) -> bool:
        # Lets go CRAZY verbose. So tolower, no slicing/reversing

        # processed_s = []
        # for char in s:
        #     if char in string.ascii_uppercase: # could even make this set myself, just {"A", "B"...}
        #         processed_s.append(chr(ord(char) - ord("A") + ord("a")))
        #     elif char in string.ascii_lowercase or char in string.digits:
        #         processed_s.append(char)
        
        # for i in range(len(processed_s)//2):
        #     if processed_s[i] != processed_s[len(processed_s) - i - 1]:
        #         return False
        
        # return True


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         return (x := [char.lower() for char in s if char in string.ascii_letters or char in string.digits]) == x[::-1]
         