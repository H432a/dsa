class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        while n>0:
            r = n%10
            sum += r
            product*=r
            n//=10
        return product-sum