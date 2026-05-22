class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ''' for all strings look at the characters they have, 
        make a set of those characters, 
        look if the set list has the set already,
        if they do have the set, then 
        make a set of those characters,
        put the sets in a list, then add '''
        map_list = []
        # [{'c':1, 'a':1, 't':1}]
        words = []
        # words = [['cat', 'act']]
        for word in strs:
            word_map = {}
            for char in word:
                word_map[char] = word_map.get(char, 0) + 1
            if word_map in map_list:
                for i in range(len(map_list)):
                    if map_list[i]==word_map:
                        words[i].append(word)
                        continue
            else:
                map_list.append(word_map)
                words.append([word])
        return words


        