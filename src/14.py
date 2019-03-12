class Solution(object):
    def longestCommonPrefix(self, strs):
        length = len(strs)
        if length == 1:
            return strs[0]
        res = ''
        temp = ''
        i = 0
        j = 0
        k = 0
        while(i+1<length):
            if(strs[i] and strs[i+1]):
                if(j<len(strs[i]) and j<len(strs[i+1])):
                    if strs[i][j] == strs[i+1][j]:
                        temp = strs[i][j]
                        k+=1
                    elif strs[i][j] != strs[i+1][j]:
                        return res;
                    elif(k==i):
                        res += temp
                        i=0
                        j=j+1
            if(i+1 == length):
                i=0
            i+=1

        return res


if __name__ == "__main__":
    a = Solution()
    i = ["flower","flow","flight"]
    r = a.longestCommonPrefix(i)
    print 'result : "'+r+'"'