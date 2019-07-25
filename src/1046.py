import heapq
class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        while len(stones)>1:
            heapq._heapify_max(stones)
            print(stones)
            max1 = heapq.heappop(stones)
            heapq._heapify_max(stones)
            max2 = heapq.heappop(stones)
            print(max1,max2)
            heapq.heappush(stones,max1-max2)
        print(stones)

if __name__ == '__main__':
    sol = Solution()
    sol.lastStoneWeight([2,7,4,1,8,1])