class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 1:      # guard clause for edge case
            return x

        l = 0
        r = x//2        # floor div. to return an integer.
                        # sqrt(x) is always <= x/2.
        while l <= r:

            mp = (r + l) // 2
            square = mp * mp
            square_minus = (mp - 1) * (mp - 1)

            if square > x and square_minus < x:     # catch nearest square root, if actual is a float
                return mp - 1

            if square > x:
                r = mp - 1
            elif square < x:
                l = mp + 1
            else:
                return mp

        return -1

        # n = x
        # Time Complexity: O(log(n//2)) ≈ O(log n)
        # Space Complexity: O(1)