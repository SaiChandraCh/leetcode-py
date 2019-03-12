class Solution(object):
    def strStr(self, haystack, needle):
        if (haystack and needle):
            if len(haystack.split(needle)) > 1:
                return len(haystack.split(needle)[0])
            else:
                return -1
        elif (not needle):
            return 0
        elif (not haystack):
            return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
