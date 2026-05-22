class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i]+=1
        output = []
        for key in counts:
            if len(output)<k:
                output.append(key)
            else:
                minim = min(output, key=lambda x:counts[x])
                print(minim)
                print(counts[key])
                if counts[key]>counts[minim]:
                    output.remove(minim)
                    output.append(key)
        return output
