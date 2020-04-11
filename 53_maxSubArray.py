class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i > 0:
                nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)


solution = Solution()
print solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
