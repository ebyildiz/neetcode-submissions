class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = []
        freqs = {}
        for i in nums:
            freqs[i] = freqs.get(i, 0) + 1
        for i in range(k):
            max_key = max(freqs, key=freqs.get)
            topk.append(max_key)
            freqs.pop(max_key)
        return topk



            
