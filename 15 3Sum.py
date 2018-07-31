class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 用了一种复杂的方式避免重复
        # used a complicated method to avoid duplicate triplets
        result = []
        result_set = set()
        nums.sort()
        index1 = set()
        for i in range(len(nums)):
            last_changed = 0
            index2 = set()
            index3 = set()
            # nums is sorted, if current number > 0, all the numbers after current number > 0.
            if nums[i] > 0:
                break
            if nums[i] not in index1:
                index1.add(nums[i])
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] not in index2 or nums[right] not in index3:
                        index2.add(nums[left])
                        index3.add(nums[right])
                        if nums[left] + nums[right] == -nums[i]:
                            result.append([nums[i], nums[left], nums[right]])
                            left += 1
                            right -= 1
                            last_changed = 0
                        elif nums[left] + nums[right] < -nums[i]:
                            last_changed = -1
                            left += 1
                        else:
                            last_changed = 1
                            right -= 1
                    else:
                        if last_changed <= 0:
                            left += 1
                        if last_changed >= 0:
                            right -= 1

        return result

s = Solution()
A= [5,-3,4,5,-1,6,-6,0]
print(s.threeSum(A))



