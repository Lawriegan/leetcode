def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []

    res = helper(res, '', n, n)
    return res

def helper(res, temp_str, left_avai, right_avai):
    if left_avai == 0:
        while right_avai > 0:
            temp_str += ')'
            right_avai -= 1
        res.append(temp_str)
        return
    elif left_avai == right_avai:
        helper(res, temp_str + '(', left_avai - 1, right_avai)
    else:
        helper(res, temp_str + '(', left_avai - 1, right_avai)
        helper(res, temp_str + ')', left_avai, right_avai - 1)
    return res
a = generateParenthesis(3)
b = 0
