class Solution(object):
    def addBinary(self, a, b):
        if not a:
            return b
        if not b:
            return a

        aLen = len(a) - 1
        bLen = len(b) - 1
        carry = "0"
        res = ""
        s = ""
        # a = 0 + b = 0 + carry = 0 => res=0 carry = 0
        # a = 1 + b = 0 + carry = 0 => res=1 carry = 0
        # a = 0 + b = 1 + carry = 0 => res=1 carry = 0
        # a = 1 + b = 1 + carry = 0 => res=0 carry = 1
        # a = 0 + b = 0 + carry = 1 => res=1 carry = 0
        # a = 1 + b = 0 + carry = 1 => res=0 carry = 1
        # a = 0 + b = 1 + carry = 1 => res=0 carry = 1
        # a = 1 + b = 1 + carry = 1 => res=1 carry = 1

        while aLen >= 0 and bLen >= 0:
            if a[aLen] == "0" and b[bLen] == "0" and carry == "0":
                carry = "0"
                res = "0"
            elif a[aLen] == "1" and b[bLen] == "0" and carry == "0" or a[aLen] == "0" and b[bLen] == "1" and carry == "0":
                carry = "0"
                res = "1"
            elif a[aLen] == "1" and b[bLen] == "1" and carry == "0":
                carry = "1"
                res = "0"
            elif a[aLen] == "0" and b[bLen] == "0" and carry == "1":
                carry = "0"
                res = "1"
            elif a[aLen] == "1" and b[bLen] == "0" and carry == "1" or a[aLen] == "0" and b[bLen] == "1" and carry == "1":
                carry = "1"
                res = "0"
            elif a[aLen] == "1" and b[bLen] == "1" and carry == "1":
                carry = "1"
                res = "1"
            s = res + s
            aLen -= 1
            bLen -= 1

        while bLen >= 0:
            if b[bLen] == "0" and carry == "1":
                carry = "0"
                res = "1"
            elif b[bLen] == "1" and carry == "1":
                carry = "1"
                res = "0"
            elif carry == "0":
                s = b[bLen] + s
                bLen -= 1
                continue
            s = res + s
            bLen -= 1

        while aLen >= 0:
            if a[aLen] == "0" and carry == "1":
                carry = "0"
                res = "1"
            elif a[aLen] == "1" and carry == "1":
                carry = "1"
                res = "0"
            elif carry == "0":
                s = a[aLen] + s
                aLen -= 1
                continue
            s = res + s
            aLen -= 1

        if carry=="1":
            return carry + s
        else:
            return s

if __name__ == "__main__":
    obj = Solution()
    print obj.addBinary("11","1")