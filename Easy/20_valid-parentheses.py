class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"(":")", "[":"]", "{":"}"}

        for c in s: # O(n) time
            if c in matching: # O(1) time
                stack.append(c) # O(n) space

            elif len(stack) == 0: # length is member function of stack, O(1) time
                return False

            elif matching[stack.pop()] != c: # O(2) time
                return False
        
        if len(stack) == 0:
            return True
        
        return False

# n = len(s)
# Space Complexity: O(n)
# Time Complexity: O(n)