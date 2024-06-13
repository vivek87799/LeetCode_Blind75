from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        output = -1
        l,r = 0, len(nums)-1

        while l<=r:
            # find mid point
            m=(r+l) // 2
            #check if t is the mid 
            if target == nums[m]:
                return m

            # check if left sorted
            if nums[l] <= nums[m]:
                # check if target lies in the left sorted
                if target >= nums[l] and target < nums[m]:
                    r=m-1
                else:
                    l=m+1
            else:
                if target > nums[m] and target <= nums[r]:
                    l=m+1
                else:
                    r=m-1
        return output