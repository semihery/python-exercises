class Solution(object):
    def findDifference(self, nums1, nums2):
        
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        answer = [[],[]]
        answer[0] = list(nums1)
        answer[1] = list(nums2)
        
        for i in nums1:
            if i in nums2:
                answer[0].remove(i)
                answer[1].remove(i)
                nums2.remove(i)
        
        for i in nums2:
            if i in nums1:
                answer[0].remove(i)
                answer[1].remove(i)

        return answer

        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        