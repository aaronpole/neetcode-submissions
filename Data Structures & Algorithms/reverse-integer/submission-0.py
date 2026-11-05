class Solution:
    def reverse(self, x: int) -> int:
        org = x
        x = str(abs(x))
        res = int(x[::-1])
        if org < 0:
            res *= -1
        if res <-(1<<31) or res > (1 << 31) - 1:
            return 0
        return res

        