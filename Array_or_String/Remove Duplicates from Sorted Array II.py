class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r=0,0
        while r<len(nums):
            count=nums.count(nums[r])
            for i in range(min(2,count)):
                nums[l]=nums[r]
                l=l+1
            r=r+(count)
        return l
