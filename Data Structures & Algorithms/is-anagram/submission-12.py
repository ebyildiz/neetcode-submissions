class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = []
        copy_t = t
        for i in s:
            if i in copy_t:
                copy_t = copy_t.replace(i, "", 1)
            else:
                return False
        if copy_t=="":
            return True
        return False
        