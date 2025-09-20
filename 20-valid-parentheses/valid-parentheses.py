class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        combo = {'(':')','[':']','{':'}'}
        expect = []
        if len(s) <= 1:
            return False

        for i in s :
            if i not in ")]}":
                expect.append(combo[i])
            else :
                if len(expect) != 0 and i == expect[-1]  :
                    expect = expect[:-1]
                else :
                    return False
        if len(expect) == 0:
            return True
        else :
            return False
        