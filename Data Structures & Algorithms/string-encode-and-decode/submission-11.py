class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        if strs==[]:
            return 'emptylist'
        for word in strs:
            encoding = ''
            for char in word:
                encoding+= str(ord(char)) + 'char'
            if word == '':
                encoding += 'emptychar'
            out.append(encoding)
        return 'word'.join(out)
            


    def decode(self, s: str) -> List[str]:
        if s=='emptylist':
            return []
        encodings = s.split('word')
        out=[]
        for e in encodings:
            word=''
            chars = e.split('char')[:-1]
            for char in chars:
                if char!='empty':
                    word+=chr(int(char))
            out.append(word)
        return out

