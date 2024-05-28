"""
53. Maximum Subarray

Given an integer arr`ay nums, find the
subarray
with the largest sum, and return its sum.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        sub_array_sum=0
        max_sub_array=float('-inf')

        for num in nums:
            sum_val = sub_array_sum+num
            max_sub_array=max(max_sub_array, sum_val)
            if sum_val < 0:
                sub_array_sum = 0
            else:
                sub_array_sum = sum_val
            
        
        return max_sub_array