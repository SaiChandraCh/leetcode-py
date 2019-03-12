class Solution(object):
    def maxSubArray(self, nums):
        temp = 0
        sum = 0
        count = 0
        if len(nums) == 1:
            return nums[0]
        else:
            for num in nums:
                temp = temp + num
                if (temp < 0):
                    temp = 0
                    count += 1
                if (temp > sum):
                    sum = temp

        if count == len(nums):
            temp = nums[0]
            for num in nums:
                if (temp < num):
                    temp = num
            sum = temp
        return sum
if __name__ == "__main__":
    obj = Solution()
    print obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])