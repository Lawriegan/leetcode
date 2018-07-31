class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        puncStack = []
        puncLeftDict = {'(':0, '[':1, '{':2}
        puncRightDict = {')':0, ']':1, '}':2}
        result = True
        for parenthese in s:
            if parenthese in puncLeftDict.keys():
                puncStack.append(parenthese)
            elif parenthese in puncRightDict.keys():
                if len(puncStack) == 0:
                    result = False
                    break
                if puncRightDict[parenthese] == puncLeftDict[puncStack[-1]]:
                    puncStack.pop(-1)
                else:
                    result = False
                    break
            else:
                result = False
                break
        if len(puncStack) != 0:
            result = False
        return result



