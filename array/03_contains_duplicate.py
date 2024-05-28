"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                return True
            num_dict[num]=1
        return False