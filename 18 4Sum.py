import time
start = time.time()
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i-1] == nums[i]: continue
            if nums[i] * 4 > target: break

            for j in range(i+1, len(nums)-2):
                if (j > i + 1 and nums[j-1] == nums[j]) or nums[i] + nums[-1] * 3 < target:
                    continue
                if nums[i] + 3 * nums[j] > target: break
                k , l = j + 1, len(nums) - 1

                while k < l:
                    if l < len(nums) - 1 and nums[l] == nums[l+1]:
                        l -= 1
                        continue
                    if k > j + 1 and nums[k-1] == nums[k]:
                        k += 1
                        continue
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        result.append([nums[i],nums[j], nums[k], nums[l]])
                        l -= 1
                        k += 1
                    elif sum > target:
                        l -= 1
                    else:
                        k += 1

        return result

num = [-483,-476,-475,-460,-450,-431,-428,-419,-410,-374,-347,-345,-311,-303,-299,-286,-278,-271,-260,-257,-240,-227,-217,-203,-196,-191,-189,-179,-171,-151,-150,-144,-134,-130,-112,-107,-97,-96,-94,-70,-62,-54,-38,-38,-23,-12,-11,-2,2,4,30,33,38,51,51,54,69,90,108,111,112,112,121,129,163,182,184,194,198,199,210,228,229,232,236,237,249,249,259,282,303,312,317,329,329,342,349,368,375,380,384,393,420,433,441,446,460,474,497]


target = -2306
s = Solution()
print('time used %f'%((time.time() - start)*1000.0))
print(s.fourSum(num, target))
