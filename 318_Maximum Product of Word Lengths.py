class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        char2int = []

        for word in words:    # 用二进制表示每个单词所含字母，位与运算为0表示两个单词不含相同字符
            num = 0
            alphabet = [0] * 26
            for char in word:
                alphabet[ord(char) - ord('a')] = 1
            for letter_idx in range(len(alphabet)):
                if alphabet[letter_idx] == 1:
                    num += 1 << letter_idx
            char2int.append(num)

        maxLen = 0
        size = len(char2int)
        for i in range(size-1):
            for j in range(i+1, size):
                length_product = len(words[i]) * len(words[j])
                if char2int[i] & char2int[j] == 0 and length_product > maxLen:
                    maxLen = length_product
        return maxLen

s = Solution()
words = ["a","aa","aaa","aaaa"]
print(s.maxProduct(words))
