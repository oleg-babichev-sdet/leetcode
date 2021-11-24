class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = 0
        for i, elem in enumerate(nums):
            count = nums.count(elem)
            if count ==1:
                res =elem
        return res
        
