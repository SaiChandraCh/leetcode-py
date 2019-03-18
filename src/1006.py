class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = ""
        if N == 0:
            return N
        index = 0
        operators = ["*","/","+","-"]
        while N > 0:
            if index == 4:
                index = 0
                continue
            if N == 1:
                s += str(N)
                N -= 1
                continue
            s += str(N) + operators[index]
            N -= 1
            index +=1
        return eval(s)

if __name__ == "__main__":
    obj = Solution()
    print obj.clumsy(0)


