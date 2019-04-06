class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)
        length = len(nums)
        while start <= end:
            mid = start + (end-start)//2
            if mid%2 == 0:
                if mid+1 < length and nums[mid] == nums[mid+1]:
                    start = mid
                elif mid-1 >= 0 and nums[mid] == nums[mid-1]:
                    end = mid
                else:
                    return nums[mid]
            else:
                if mid+1 < length and nums[mid] == nums[mid+1]:
                    end = mid
                elif mid-1 >= 0 and nums[mid] == nums[mid-1]:
                    start = mid
                else:
                    return nums[mid]

if __name__ == '__main__':
    obj = Solution()
    print(obj.singleNonDuplicate([1,1,2,2,3,4,4]))