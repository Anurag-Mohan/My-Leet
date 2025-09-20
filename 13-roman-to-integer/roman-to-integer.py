class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rdict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev = s[-1]
        sums = 0
        for i in s[::-1]:
            if rdict[i] >= rdict[prev] :
                sums += rdict[i]
                prev = i
            else :
                sums -= rdict[i]
                prev = i
        return sums
