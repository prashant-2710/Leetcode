class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1

        rev = int(str(abs(x))[::-1]) * sign   
        # First converting the number into absolute value then into string then reversing the string then again converting number into integer to multiply it with the sign 

        # 32-bit signed integer boundary check
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
            
        return rev