class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        while K >0 :
            index = 0
            min = A[0]
            temp = 0
            for a in A:
                if(min > a):
                    min = a
                    index = temp
                temp +=1
            print A,"index : ",index
            A[index] = -A[index]
            K-=1

        print A
        return sum(A)

if __name__ == "__main__":
    obj = Solution()
    print obj.largestSumAfterKNegations([3,-1,0,2],3)