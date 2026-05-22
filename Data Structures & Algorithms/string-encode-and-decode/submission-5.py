class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        if strs == ['']:
            return 'empty: special case'
        encodings = []
        for word in strs:
            encoding = ''
            for letter in word:
                encoding+= str(ord(letter))+" delimiter "
            encodings.append(encoding)
        
        return ' array '.join(encodings)
            


    def decode(self, s: str) -> List[str]:
        if s=='empty: special case':
            return ['']
        if s=='':
            return []
        lst = s.split(' array ')
        decodings = []
        for word in lst:
            decoding = ''
            chars = word.split(' delimiter ')
            chars.remove('')
            print(chars)
            for i in chars:
                decoding += chr(int(i))
            decodings.append(decoding)
        return decodings

