class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=dict()
        output=[]
        for word in strs:
            chars = list(word)
            key = ''.join(sorted(chars))
            if key in groups.keys():
                groups[key].append(word)
            else:
                groups[key] = [word]
        return groups.values()
         


#intuitive approach:
# for each string check if the letters of it exist in any of the given characters
