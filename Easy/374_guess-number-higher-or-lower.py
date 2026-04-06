class Solution:
    def guessNumber(self, n: int) -> int:

        r = n
        l = 1

        while True:

            k = (l + r) // 2

            if guess(k) == -1:
                r = k - 1           # prevent repeated comparisions & infinite loop
            elif guess(k) == 1:
                l = k + 1           # same as above
            else:
                return k

# O(logn) time. Happens when target num k is either 1 or n.
# O(1) space