class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        p = range(1,m+1)
        result = []
        for i in queries:
            result.append(p.index(i))
            k = p.pop(p.index(i))
            p.insert(0,k)
        return result

        