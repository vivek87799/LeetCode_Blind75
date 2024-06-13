class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = float('inf')
        l,r = 0, len(nums)-1

        while l<=r:

            if nums[l]<=nums[r]:
                return min(min_val, nums[l])
            m=(l+r) // 2

            if nums[l]<=nums[m]:
                min_val = min(min_val, nums[l])
                l=m+1
            else:
                min_val = min(min_val, nums[m])
                r = m-1
            
        return min_val