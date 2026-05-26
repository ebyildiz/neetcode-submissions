class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = []
        freqs = {}
        for i in nums:
            freqs[i] = freqs.get(i, 0) + 1
        heap = []
        for num in freqs.keys():
            heapq.heappush(heap, (freqs[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(k):
            topk.append(heapq.heappop(heap)[1])

        return topk


            
