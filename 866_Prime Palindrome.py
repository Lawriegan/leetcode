import math
class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1 or N == 2:
            return 2
        if (1e7 <= N and N <= 1e8):
            print('111')
            return 100030001

        if N % 2 == 0:
            N += 1
        while True:
            if self.isPalindrome(N):
                if self.isPrime(N):
                    return N
            N += 2

    def isPrime(self, num):
        for i in range(3, int(math.sqrt(num))+1, 2):
            if num % i == 0:
                return False
        return True

    def isPalindrome(self, num):
        string = str(num)
        while len(string) > 1:
            if string[0] != string[-1]:
                return False
            else:
                string = string[1:-1]
        return True

s = Solution()
print(s.primePalindrome(9989900))
