"""
# Approach
<!-- Describe your approach to solving the problem. -->

1. `l` and `r` are initialized as two pointers representing the leftmost and rightmost lines of the container. `l` starts from the leftmost line (index 0), and `r` starts from the rightmost line (index len(height)-1).
2. `area` is initialized to 0, which will be used to store the maximum area found so far.

The algorithm uses a while loop that continues until `l` becomes greater than or equal to `r`. During each iteration of the loop, the current area is calculated based on the height of the lines at positions `l` and `r`. The minimum height between the two lines is taken (min(height[l], height[r])), and it's multiplied by the width of the container (r - l). The maximum of this current area and the previously found maximum area is then stored in the `area` variable.

The algorithm proceeds by moving the pointers `l` and `r` towards each other to explore different combinations of lines. At each step, the pointer corresponding to the shorter line is moved inward. This is because moving the pointer corresponding to the taller line won't increase the area since the width of the container decreases. The algorithm aims to find the best combination of lines that maximize the container's area.

Finally, when `l` becomes greater than or equal to `r`, the loop terminates, and the maximum area found is returned.

# Complexity
-Time Complexity:
The two-pointer approach only needs a single pass through the input array, so the time complexity is O(n), where n is the number of elements in the `height` array.

-Space Complexity:
The space complexity is O(1) since the algorithm uses only a constant amount of extra space to store variables `l`, `r`, and `area`. It does not use any additional data structures that grow with the input size.



# Code"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        area=0

        while l<r:
            curr=min(height[l],height[r])*(r-l)
            area=max(area,curr)

            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return area
        
