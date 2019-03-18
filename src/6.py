class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        str = ""
        length = len(s)
        j = 0
        i = 0
        index = 0
        res = [[] for _ in range(numRows)]
        vert = True
        diag = False
        while length > 0:
            if vert:
                if i == numRows-1:
                    vert = False
                    diag = True
                else :
                    res[i].insert(j,s[index])
                    i += 1
                    index += 1
                    length -= 1

            if diag:
                if i == 0:
                    vert = True
                    diag = False
                else:
                    res[i].insert(j,s[index])
                    i -= 1
                    j += 1
                    index += 1
                    length -= 1
        for row in res:
            for cell in row:
                str += "" + cell

        return str

if __name__ == "__main__":
    obj = Solution()
    print obj.convert("PAYPALISHIRING",4)