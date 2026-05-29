class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res
    def decode(self, s: str) -> List[str]:
        length = ""
        words = []
        i = 0
        while i<len(s):
            if s[i]=='#':
                word = s[i+1 : i+1+int(length)]
                words.append(word)
                i = i+1+ int(length)
                length=""
            else:
                length+=s[i]
                i+=1
        return words
