# 01-28-2024 Neetcode 271. Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings/
# Time: 5 Mins

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for next_string in strs:
            encoded += str(len(next_string)) + ":" + next_string
        
        return encoded
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []

        i = 0
        while i < len(s):
            next_string_len = 0
            while s[i] in string.digits:
                next_string_len = next_string_len * 10 + int(s[i])
                i += 1
            i += 1 #skip our delimeter- this char must be ":" if not a digit, no need to check it
            decoded.append(s[i:i+next_string_len]) 
            i += next_string_len
        
        return decoded
