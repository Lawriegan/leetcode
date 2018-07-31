class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_list = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        if len(digits) == 0:
            return []

        def map2num(button1, button2):
            return [char1+char2 for char1 in button1 for char2 in button2]
        #cur_list = map_list[int(digits[0])]
        cur_list = ['']
        for i in range(0,len(digits)):
            cur_list = map2num(cur_list, map_list[int(digits[i])])
        return cur_list

print(Solution().letterCombinations('2'))
