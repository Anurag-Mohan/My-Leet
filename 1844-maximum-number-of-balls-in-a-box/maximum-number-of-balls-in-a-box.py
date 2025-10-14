from collections import defaultdict
class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        boxes = defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            s = sum(int(j) for j in str(i))
            boxes[s] += 1
        
        return boxes[max(boxes, key=boxes.get)]

        