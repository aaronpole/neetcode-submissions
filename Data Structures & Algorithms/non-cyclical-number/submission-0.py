class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            output = 0
            while n > 0:
                digit = n % 10
                output += digit*digit
                n //= 10
            return output
        slow = n
        fast = sumOfSquares(n)
        while slow != fast:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
        if fast == 1:
            return True
        return False