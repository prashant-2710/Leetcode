class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rev_x = s[::-1]
        if s == rev_x:
            return True
        return False