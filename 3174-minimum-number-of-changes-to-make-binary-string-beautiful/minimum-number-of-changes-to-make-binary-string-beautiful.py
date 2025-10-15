from collections import Counter
class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        minChange = 0
        l = len(s)
        subl = [ s[i:i+2] for i in range(0,l,2)]
        for i in subl:
            if '0' in i and '1' in i :
                minChange += min(Counter(i).values())
        return minChange

