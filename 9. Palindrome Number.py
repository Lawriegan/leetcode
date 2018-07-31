def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    '''
    max = "2147483647"
    if x < 0:
        return False
    s = str(x)
    if (len(s) > 10 or (len(s)==10 and s > max)):
        return False
    i = 0;j = len(s) - 1
    while (i <= j):
        if (s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True
    '''
    return int(str(abs(x))[::-1]) == x
for i in [-2,-525,2,0,525,666]:
    print(isPalindrome(i))
