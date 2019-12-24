class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        data_set = set()
        for n in nums:
            if n in data_set:
                return True
            data_set.add(n)
        return False