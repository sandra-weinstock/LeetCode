class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if len(nums1) == 0 or len(nums2) == 0:
            return

        i = m - 1
        j = n - 1
        
        while i >= 0 and j >= 0: # O (m + n - 1) or O(m)
            if nums1[i] > nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            else:
                nums1[i + j + 1] = nums2[j]
                j -= 1

        while j >= 0: # O (1) or O(n)
            nums1[j] = nums2[j]
            j -= 1

        # Time Complexity : O(m + n) ≈ O(z)
        # Space Complexity : O(2) ≈ O(z)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        if len(nums1) == 0 or len(nums2) == 0:
            return

        i = m - 1
        j = n - 1

        while j >= 0:

            if i >= 0 and nums1[i] > nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            else:
                nums1[i + j + 1] = nums2[j]
                j -= 1

        # Time Complexity: O(n + m) ≈ O(z), number of comparisons = m
        # Space Complexity: O(2) ≈ O(1)