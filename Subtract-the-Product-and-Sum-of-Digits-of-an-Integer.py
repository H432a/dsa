class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        product = 1
        while n>0:
            r = n%10
            summ += r
            product*=r
            n//=10
        return product-summ