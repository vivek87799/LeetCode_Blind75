"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*(len(nums)+1)
        postfix=[1]*(len(nums)+1)
        output = [1] * len(nums)
        for i in range(1, len(prefix)):
            prefix[i]=nums[i-1]*prefix[i-1]
        nums_rev = nums[::-1]
        for i in range(1, len(postfix)):
            postfix[i]=nums_rev[i-1]*postfix[i-1]
        postfix = postfix[::-1]

        for i in range(0, len(output)):
            output[i]=prefix[i]*postfix[i+1]
        return output