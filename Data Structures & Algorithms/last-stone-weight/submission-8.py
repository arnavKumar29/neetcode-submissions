class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[-stone for stone in stones]
        heapq.heapify(max_heap)
        ans=0
        while len(max_heap)>1:
            first=-heapq.heappop(max_heap)
            second=-heapq.heappop(max_heap)
            if(first==second):
                continue

            
            elif(first<second):
                bruh=second-first
                heapq.heappush(max_heap,-bruh)
                
            else:
                bruh2=first-second
                heapq.heappush(max_heap,-bruh2)
        if not max_heap:
            return 0
        return -max_heap[0]

        