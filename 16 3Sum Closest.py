class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = nums[0]+nums[1]+nums[2]
        min_diff = abs(closest_sum - target)
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1]==nums[i]: continue
            j = i + 1
            k = len(nums) - 1
            cur_max_sum = nums[i] + nums[k-1] + nums[k]
            cur_min_sum = nums[i] + nums[j] + nums[j+1]
            if cur_max_sum < target and abs(cur_max_sum - target) < min_diff:
                min_diff = abs(cur_max_sum - target)
                closest_sum = cur_max_sum
                continue
            if cur_min_sum > target and abs(cur_min_sum - target) < min_diff:
                min_diff = abs(cur_min_sum - target)
                closest_sum = cur_min_sum
                continue
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if abs(cur_sum - target) < min_diff:
                    min_diff = abs(cur_sum - target)
                    closest_sum = cur_sum
                if cur_sum == target:
                    return target
                elif cur_sum < target:
                    j += 1
                else:
                    k -= 1
        return closest_sum


s = Solution()
num = [-10,0,-2,3,-8,1,-10,8,-8,6,-7,0,-7,2,2,-5,-8,1,-4,6]
print(s.threeSumClosest(num,18))
