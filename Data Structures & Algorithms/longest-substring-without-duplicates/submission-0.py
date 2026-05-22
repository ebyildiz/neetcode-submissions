class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left = 0
        longest_s = 0
        for i, c in enumerate(s):
            if c in chars:
                right = chars[c]+1
                for ch in s[left:right]:
                    chars.pop(ch)
                chars[c] = i
                left = right
            else:
                chars[c] = i
                curr_length = len(chars)
                longest_s = max(curr_length, longest_s)
        return longest_s

