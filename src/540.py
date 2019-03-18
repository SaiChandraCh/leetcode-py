class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        i = 0
        if nums:
            while i+1 < length:
                if nums[i]^nums[i+1] != 0:
                    return nums[i]
                i += 2
            return nums[i]
        else:
            return 0