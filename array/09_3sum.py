from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        i=0
        while i < len(nums)-1:
            if i > 0 and nums[i]==nums[i-1]:
                i+=1
                continue             

            l=i+1
            r=len(nums)-1

            while l<r:
                
                sum_val = nums[i]+nums[l]+nums[r]
                if sum_val < 0:
                    l+=1
                elif sum_val > 0:
                    r-=1
                else:
                    output.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l <r and nums[l]==nums[l-1]:
                        l+=1
                    while r<r and nums[r]==nums[r-1]:
                        r-=1
            i+=1
        return output
