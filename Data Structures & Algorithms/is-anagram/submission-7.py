class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = list(s)
        letters_t = list(t)
        if len(s)!=len(t):
            return False
        for i in letters_s:
            if i in letters_t:
                letters_t.remove(i)
            else:
                return False
        return True
        