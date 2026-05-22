class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        words = []
        for word in strs:
            sorted_word = sorted(word)
            if sorted_word in anagrams:
                words[anagrams.index(sorted_word)].append(word)
            else:
                anagrams.append(sorted_word)
                words.append([word])
        
        return words