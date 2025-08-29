class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31


        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
            
        a,b = abs(dividend), abs(divisor)
        result = 0

        while a>= b:
            shift = 0 
            while a >= b << (shift + 1):
                shift += 1
            a-= b<<shift
            result += 2**shift
        if (dividend < 0) ^ (divisor < 0):
            result = -result
        return result