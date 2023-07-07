class Solution(object):
    def majorityElement(self, nums):
        l,r=0,0
        sorted(nums)
        while r<len(nums):
            count=nums.count(nums[r])
            if(count>(len(nums)/2)):
                return nums[r]
            r=r+count
