class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} #use defaultdict instead so that the default value is always a list to not deal with append
        #the alphabet dictionary
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        d={} 
        for i in range(26):
            d[alpha[i]] = i
        # instead of this you can make use of ord() function
        for word in strs:
            array_map = ['0']*26
            for char in word:
                array_map[d[char]] = str (int(array_map[d[char]]) + 1)
            key = '-'.join(array_map) #change to tuple instead of turning into a string
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return groups.values()            
         
