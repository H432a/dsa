class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x = abs(x)
        n = 0

        while x>0:
            a = x%10
            n = n*10 + a
            x //= 10

        n *= sign

        if n < -2**31 or n > 2**31 - 1 :
            return 0

        return n
            