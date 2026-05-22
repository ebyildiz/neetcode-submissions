class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ss = set(s)
        st = set(t)
        if ss!=st:
            return False
        for i in ss:
            if s.count(i)!=t.count(i):
                return False
        return True
