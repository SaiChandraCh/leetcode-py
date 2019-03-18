class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        done = True
        carry = 0
        index = len(digits)-1
        while not done and index >= 0:
            carry
            if (carry == 0):
                done = False

if __name__ == "__main__":
    obj = Solution()
    obj.plusOne([9,9,9])