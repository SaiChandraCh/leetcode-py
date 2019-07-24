class Solution:
    def minDeletionSize(self, A: [str]) -> int:
        if A and len(A[0]) <= 1:
            return 0
        length = len(A)
        strLen = len(A[0])
        deleted = []
        for i in range(length -1):
            j = i+1
            for k in range(strLen):
                print(A[i][k],A[j][k],A[i][k]>A[j][k])
                if k not in deleted and A[i][k]>A[j][k]:
                    deleted.append(k)
        return len(deleted)

if __name__ == '__main__':
    sol = Solution()
    print(sol.minDeletionSize(["cba","daf","ghi"]))
