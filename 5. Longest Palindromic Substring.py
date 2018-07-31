def longestPalindrome(s):
    maxl = maxt = 1
    maxlength = 1
    loc = 0
    l = 0; t = 0
    for i in range(len(s)):
        while(i-l>=0 and i+l+1<len(s) and s[i-l]==s[i+l+1]):
            if s[i-l]==s[i+l+1]:
                l += 1
                maxl = 2*l

        while(i-t>=0 and i+t<len(s) and s[i-t]==s[i+t]):
            if s[i-t]==s[i+t]:
                t += 1
                maxt = 2*t-1
        if max(maxl,maxt) > maxlength:
            loc = i
            maxlength = max(maxl,maxt)
        l = 0;t = 0
    left = loc-(maxlength-1)//2
    return s[left:left+maxlength]
for s in ["","a","aa","aaa","babad","abcba","dbcbcb","tfghhhuk"]:
    print(longestPalindrome(s))

#another answer
'''
def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)
        return res
             
    def helper(self,s,l,r):     
        while 0<=l and r < len(s) and s[l]==s[r]:
                l-=1; r+=1
        return s[l+1:r]
'''
