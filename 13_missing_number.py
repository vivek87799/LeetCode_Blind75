"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_dict = {key:1 for key in range(0, len(nums)+1)}
        for n in nums:
            del num_dict[n]
        return list(num_dict.keys())[0]