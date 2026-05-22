class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        d={}
        for i in range(26):
            d[alpha[i]] = i
        for word in strs:
            array_map = ['0']*26
            for char in word:
                string_val = array_map[d[char]]
                array_map[d[char]] = str (int(string_val) + 1)
            key = '-'.join(array_map)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return groups.values()            
         
