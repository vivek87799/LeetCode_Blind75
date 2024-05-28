"""
152. Maximum Product Subarray

Given an integer array nums, find a
subarray
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        prod=1

        for num in nums:
            prod=prod*num
            max_prod=max(prod, max_prod)
            if prod == 0:
                prod =1
        
        prod = 1
        for num in nums[::-1]:
            prod=prod*num
            max_prod=max(prod, max_prod)
            if prod==0:
                prod=1

        
        return max_prod