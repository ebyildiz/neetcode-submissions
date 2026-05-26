class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for i in nums:
            freqs[i] = freqs.get(i, 0) + 1

        maxim = max(freqs.values()) + 1

        buckets = [[] for i in range(maxim)]
        
        for i in freqs.keys():
            bucketno = freqs[i]
            buckets[bucketno].append(i)
        
        topk = []

        buckets_reversed = buckets[::-1]

        for i in buckets_reversed:
            for y in i:
                topk.append(y)
                if len(topk) == k:
                    return topk
                

        
