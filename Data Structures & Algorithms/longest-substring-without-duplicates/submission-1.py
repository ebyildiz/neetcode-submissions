class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        left = 0
        longest_s = 0
        for i, c in enumerate(s):
            if c in chars:
                if chars[c]>=left: 
                    left = chars[c]+1
                    chars[c] = i
                    curr_length = i-left+1
                    longest_s = max(curr_length, longest_s)
                    continue
            chars[c] = i
            curr_length = i-left+1
            longest_s = max(curr_length, longest_s)
        return longest_s

