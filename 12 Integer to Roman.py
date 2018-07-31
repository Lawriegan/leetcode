class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        int2roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',\
                     100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        integers = sorted(int2roman.keys(), reverse=True)
        #print(integers)
        roman = ''
        while num > 0:
            for i in integers:
                while num >= i and num > 0:
                    roman += int2roman[i]
                    num -= i
                if num == 0:
                    break
        return roman

s = Solution()
ex = [1,3,4,5,9,11,15,50,41,49,50,900,999,1000]
for i in ex:
    print(s.intToRoman(i))
