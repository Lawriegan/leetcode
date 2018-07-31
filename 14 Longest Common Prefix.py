
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is []:
            return ''
        prefix = {}
        min_len = 0xffffffff
        min_len_str = ''
        for string in strs:
            if len(string) < min_len:
                min_len_str = string
                min_len = len(string)
        for i in range(min_len+1):
            prefix[min_len_str[0:i]] = 0
        for string in strs:
            for i in range(len(string)+1):
                if string[0:i] in prefix:
                    prefix[string[0:i]] += 1
        max_value = 1
        max_len_prefix = ''
        for key, value in prefix.items():
            if value > max_value and value > 1:
                max_len_prefix = key
                max_value = value
            elif value == max_value and value > 1 and len(key) > len(max_len_prefix):
                max_len_prefix = key
        return max_len_prefix
    '''
     def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
    '''
s = Solution()
sss = ["flower","flow","flight"]
sss2 = ['dog', 'a', 'cat']
print(s.longestCommonPrefix(sss2))
