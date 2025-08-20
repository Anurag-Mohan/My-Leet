class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        i = 0
        while i < len(s) and s[i].isdigit():
            i += 1
        if i == 0:
            return 0 
        
        num = int(s[:i]) * sign
        

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num