
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        length = len(nums)
        end = length - 1
        pivot = 0

        if nums:
            while start <= end:
                if end - start <= 1:
                    pivot = end
                    break
                mid = int(start + (end - start)/2)
                if nums[mid] >= nums[start]:
                    start = mid
                elif nums[mid] <= nums[end]:
                    end = mid

            if target<nums[0]:
                start = pivot
                end = length-1
            else:
                start = 0
                end = pivot

            while start <= end:
                mid = int(start + (end-start)/2)
                if target == nums[mid]:
                    return mid
                if target > nums[mid]:
                    start = mid+1
                elif target < nums[mid]:
                    end = mid-1
        return -1

if __name__ == '__main__':
    obj = Solution()
    print(obj.search([0,1],0))