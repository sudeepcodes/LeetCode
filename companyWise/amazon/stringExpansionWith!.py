"""
You are given a string consisting of characters '0', '1', and '!'.

    Each '!' can be replaced by either '0' or '1'.
    For each expansion, count the total number of subsequences "01" and "10".

Return the minimum possible count over all expansions, modulo 1e9+7.

Example: s => "0!1!"
Ouptut: 3

Explanation:
There are 2^2 = 4 expansions (replace each ! by 0 or 1):
    "0 0 1 0" → "0010"
total subsequences = 3
(explicit: "01" = 2 pairs, "10" = 1 pair)

    "0 0 1 1" → "0011"
total subsequences = 4
(explicit: "01" = 4, "10" = 0)

    "0 1 1 0" → "0110"
total subsequences =4
(explicit: "01" = 2, "10" = 2)

    "0 1 1 1" → "0111"
total subsequences = 3
(explicit: "01" = 3, "10" = 0)

Minimum total over all expansions = 3


Notes:
To calculate the number of sub-sequance[01 or 10] in a string, all we need is the number of 0's and ones, it'll always be No.of zeros*no. of ones, eg. 0101, 0011, 1100 all have 4 possible combinations

The total count will be the the product of i.e count(zeros)count(ones) to reduce it, the best way always is maximise one or zero, so if the string have more ones then we will convert all the ! also to one, also if it have more zeros then we will convert all ! to zeros

for two values which has sum of 10, the products possible are 19=9 28=16 37=21 46=24 55=25, you can see the product keeps increasing as the difference between them decrease here we apply the same concept, either convert all ! zero or one to reduce the combined product.

"""



class Solution:
    def stringExpansion(self, s: str):
        freq = {}

        for ch in s:
            if ch == '0':
                freq['0'] = 1 + freq.get('0', 0)
            elif ch == '1':
                freq['1'] = 1 + freq.get('1', 0)
            else:
                freq['!'] = 1 + freq.get('!', 0)
        
        if freq['0'] >= freq['1']:
            return (freq['0'] + freq['!']) * freq['1']
        else:
            return (freq['1'] + freq['!']) * freq['1']

print(Solution().stringExpansion("0!1!"))