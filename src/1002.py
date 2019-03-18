class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        length = len(A)
        flag = False
        list = []
        for char in A[0]:
            index = 1
            while index < length:
                if char in A[index]:
                    A[index]=A[index].replace(char,'',1)
                    flag = True
                    index += 1
                else:
                    flag = False
                    break
            if flag:
                list.append(char)
                flag = False

        return list

if __name__ == "__main__":
    obj = Solution()
    print obj.commonChars(["bella","label","roller"])
