class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        if(nums2):
            del nums1[-n:]
            nums1.extend(nums2)
            nums1.sort()
        else:
            nums1.sort()
        
        
