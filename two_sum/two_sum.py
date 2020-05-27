class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = dict()

        for i, num in enumerate(nums):
            if (target - num) in index:
                return [i, index[target - num]]
            index[num] = i
        return []
