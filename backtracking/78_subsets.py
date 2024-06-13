"""
78. Subsets
Solved
Medium
Topics
Companies

Given an integer array nums of unique elements, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.


"""

from collections import defaultdict
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        memo = defaultdict(list)
        def subsetsHelper(ind: int, arr: list[int]):

            if ind >=len(nums):
                memo[ind].append(arr[:])
                output.append(arr[:])
            else:
                subsetsHelper(ind+1, arr+[nums[ind]])
                subsetsHelper(ind+1, arr)
            
        subsetsHelper(0, [])
        return output