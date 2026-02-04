class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()   # To store numbers we have already seen

        while n != 1:

        # If n is already seen, it means we are in a loop
            if n in seen:
                return False

            seen.add(n)   # Store current number

            sum_sq = 0    # Sum of squares of digits
            temp = n

        # Calculate sum of squares of digits
            while temp > 0:
                digit = temp % 10       # Get last digit
                sum_sq += digit * digit
                temp //= 10             # Remove last digit

            n = sum_sq   # Replace n with new value

        return True   # If n becomes 1


