class Solution(object):
    def maxProfit(self, prices):
        buy = 0
        sell = 1
        profit = 0
        length = len(prices)
        while sell < length:
            if(prices[sell]>prices[buy]):
                profit += prices[sell]-prices[buy]
                buy = sell
            else:
                buy +=1
            sell +=1
        print "a"," a ","a"
        return profit

if __name__ == "__main__":
    obj = Solution()
    print obj.maxProfit([1,2,3,4,5])