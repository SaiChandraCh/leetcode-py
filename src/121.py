class Solution(object):
    def maxProfit(self, prices):
        buy = 0
        sell = 1
        profit = 0
        length = len(prices)
        while sell < length:
            if(prices[buy]>prices[sell]):
                buy = sell
            elif(prices[sell]-prices[buy]>profit):
                profit = prices[sell]-prices[buy]
            sell += 1
        return profit

if __name__ == "__main__":
    obj = Solution()
    print obj.maxProfit([7,6,4,3,1])