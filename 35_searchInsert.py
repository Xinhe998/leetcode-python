class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid = len(nums) / 2
        low, up = 0, len(nums)-1

        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        while low <= up:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                up = mid - 1
            else:
                low = mid + 1
            mid = (low+up) / 2
        return low


solution = Solution()
print solution.searchInsert([1, 3], 2)
