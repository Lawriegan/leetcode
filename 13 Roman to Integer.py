class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman2int = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, \
                     'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        i = num = 0
        length = len(s)
        while i < length:
            if s[i:i+2] in roman2int:
                num += roman2int[s[i:i+2]]
                i += 2
            else:
                num += roman2int[s[i]]
                i += 1
        return num
s = Solution()
ss = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']
for sss in ss:
    print(s.romanToInt(sss))
