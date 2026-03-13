class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        for i in range(len(s)): # O(n) time
            newS = s[:i] + s[i + 1:] # O(n - 1) space
            if newS == newS[::-1]: # O(n - 1) time
                return True
        
        return False

        # n = len(s)
        # Time Complexity: O(n^2 - n) ≈ O(n^2)
        # Space Complexity: O(n - 1) ≈ O(n)