class Solution:
    def findpower(self, x, n):
        if n == 0:
            return 1
        a = self.findpower(x, n//2)
        if n%2 == 0:
            return a*a
        else:
            return a*a*x
    def myPow(self, x: float, n: int) -> float:
        if n>=0:
            return self.findpower(x, n)
        else:
            return 1/self.findpower(x, n*(-1))