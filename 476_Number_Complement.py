class Solution:
    def findComplement(self, num: int) -> int:

        def decimal_to_binary(n):
            if n == 0:
                return 0

            res = ''
            while n > 0:
                res += str(n % 2)
                n //= 2

            return res[::-1]

        def binary_to_decimal(s):
            res = 0
            pow = 0
            for ch in s[::-1]:
                res += (2 ** pow) * int(ch)
                pow += 1
            return res

        req = decimal_to_binary(num)
        aa = []
        for i in req:
            if i == '1':
                aa.append(0)
            else:
                aa.append(1)
        return binary_to_decimal(aa)
