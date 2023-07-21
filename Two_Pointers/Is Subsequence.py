"""# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->
The Python code presents a class `Solution` with a method `isSubsequence` that checks if string `s` is a subsequence of string `t`. It employs a two-pointer technique, initializing pointers `i` and `j` to the start of both strings. The method then traverses the strings simultaneously, comparing characters at the respective positions of `i` and `j`. If a character in `s` matches the character in `t`, both pointers advance to the next characters. If there's no match, only the pointer for `t` moves ahead. This process continues until either the end of `s` is reached or the end of `t`. If `i` reaches the end of `s`, it implies that all characters in `s` were found in `t` in the same order, indicating `s` is a subsequence. In that case, the method returns `True`; otherwise, it returns `False`.

# Complexity
- The time complexity of the `isSubsequence` method is O(N), where N is the length of string `t`, and the space complexity is O(1) since the method only uses a constant amount of extra space regardless of the input size.

# Code"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #return re.search(".*".join(list(s)),t)
        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i==len(s):
            return True
        else:
            return False
