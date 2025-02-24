class Solution(object):
    def buildArray(self, nums):
        """
        Given a zero-based permutation nums (0-indexed),
        build an array ans of the same length where
        ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
        A zero-based permutation nums is an array of distinct
         integers from 0 to nums.length - 1 (inclusive).

        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for number in range(len(nums)):
            ans.append("x")

        for i in range(len(ans)):
            ans[i] = nums[nums[i]]

        return ans
