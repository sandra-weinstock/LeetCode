class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0

        while r < len(nums): # O(n) or O(1) time
            nums[l] = nums[r] # O(1) space
            r += 1

            while r < len(nums) and nums[r] == nums[l]: # O(1) or O(n) time
                r += 1

            l += 1

        return l

        # n = len(nums)
        # Time Complexity: O(n) + O(1) ≈ O(n)
        # Space Complexity: O(1)