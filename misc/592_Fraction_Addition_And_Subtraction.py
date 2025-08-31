from math import gcd


class Solution:
    def get_lcm(self, arr):
        res = 1
        for i in arr:
            res = res * int(i) // gcd(res, int(i))
        return res

    def fractionAddition(self, expression: str) -> str:
        numerators = []
        denominators = []

        if expression[0] != '-':
            expression = '+' + expression

        i = 0
        j = 1
        while j < len(expression):
            if expression[j] == '/':
                numerators.append(expression[i:j])
                i = j
            elif expression[j] in ['+', '-']:
                denominators.append(expression[i + 1:j])
                i = j
            j += 1

        denominators.append(expression[i + 1:j])
        lcm = self.get_lcm(denominators)

        num_sum = 0
        for i in range(len(numerators)):
            num_sum += int(numerators[i]) * (lcm // int(denominators[i]))

        _gcd = gcd(num_sum, lcm)
        num_sum //= _gcd
        lcm //= _gcd

        return f'{num_sum}/{lcm}'


print(Solution().fractionAddition("1/3-1/2"))
