class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = dict()
        for i in range(len(nums)):
            remaining_val = target - nums[i]
            if remaining_val in hashmap:
                return [hashmap[remaining_val], i]
            hashmap[nums[i]] = i



if __name__ == '__main__':
    l = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(l,target))