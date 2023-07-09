class Solution:
    def reverse(self, nums:List[int],start:int,end:int)->None:
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
    def rotate(self, nums: List[int], k: int) -> None:
        
        k = k % (len(nums)) 
        self.reverse(nums,0,(len(nums))-1) #reversing entire array
        self.reverse(nums,0,k-1) #reversing first half
        self.reverse(nums,k,(len(nums))-1) #reversing second half
        


        
