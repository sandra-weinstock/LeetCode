class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = [] # O(n) space
        total = 0

        for op in operations: # O(n) time
            if op == "+":
                new = record[-2] + record[-1] # 2 ops ... can't pop more than my list. at most n ops per n elts
                record.append(new)
            
            elif op == "C":
                record.pop()

            elif op == "D":
                new = 2 * record[-1]
                record.append(new)
            else:
                record.append(int(op))
        
        for n in record: # O(n) time
            total += n

        return total

# n = len(operations)
# Space Complexity: O(n)
# Time Complexity: O(2n)