class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        left = 0
        right = len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            water = max(water, h * (right - left))
            best_left, best_right = left, right
            while left < right and height[left] <= h:
                left += 1
            while left < right and height[right] <= h:
                right -= 1
        return water

s = Solution()
print(s.maxArea([1,2,4,3]))
