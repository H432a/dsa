class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman_map = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

        i = 0
        while i < len(s):
            curr = roman_map[s[i]]
            # if last numeral don't check for next
            if len(s) - i == 1:
                res += curr
                break
            next_val = roman_map[s[i + 1]]
            if curr < next_val:
                res += next_val - curr
                # we added the curr and next, so inc. 1 additional to move
                # past our current next numeral
                i += 1
            else:
                res += curr
            i += 1

        return res