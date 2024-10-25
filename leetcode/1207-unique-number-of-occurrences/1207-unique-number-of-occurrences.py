class Solution(object):
    def uniqueOccurrences(self, arr):

        nums = set(arr)
        nums = dict(zip(nums, (0 for i in range(len(nums)))))

        for i in arr:
            nums[i] += 1


        for i in range(len(nums.values())):
            if nums.values()[i] in nums.values()[i+1:]:
                return False
        
        return True

        """
        :type arr: List[int]
        :rtype: bool
        """
        