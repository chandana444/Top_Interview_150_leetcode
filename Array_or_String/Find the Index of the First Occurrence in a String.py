class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            i=0
            while i<len(haystack):
                if (haystack[i:i+len(needle)])==needle:
                    return i
                else:
                    i+=1
        return -1
