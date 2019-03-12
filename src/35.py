class Solution(object):
    def searchInsert(self, nums, target):
        index = 0
        for num in nums:
            if num < target:
                index += 1
            else:
                return index
        return index

if __name__ == "__main__":
    obj = Solution()
    r  = obj.searchInsert([1,3,5,6],2)
    print 'result : '
    print(r)
