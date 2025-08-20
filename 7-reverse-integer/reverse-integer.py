class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        s = str(abs(x))
        m = int(s[::-1]) * sign
        
        if m < -2**31 or m > 2**31 - 1:
            return 0
        return m
