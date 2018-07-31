def findMedianSortedArrays(num1, num2):
    median = 0
    if len(num1) == 0:
        return num2[len(num2)//2]
    elif len(num2) == 0:
        return num1[len(num1)//2]
    if num1[len(num1)//2] == num2[len(num2)//2]:
        median = num1[len(num1)//2]
    elif num1[len(num1)//2] < num2[len(num2)//2]:
        median = findMedianSortedArrays(num1[len(num1)//2:], num2[:len(num2)//2])
    else:
        median = findMedianSortedArrays(num1[:len(num1)//2], num2[len(num2)//2:])
    return median

num1 = [1,3,5,7,9]
num2 = [2,4,6,8,10]
print(findMedianSortedArrays(num1,num2))
