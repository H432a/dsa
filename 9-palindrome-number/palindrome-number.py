class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = 0
        dup = x
        while x>0:
            b = x%10
            a = a*10 + b
            x //= 10
        if dup == a:
            return True
        else: 
            return False
        