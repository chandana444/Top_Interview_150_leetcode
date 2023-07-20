class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short=min(strs,key=len)
        for s in strs:
            while len(short)>0:
                if(s.startswith(short)):
                    break
                else:
                    short=short[:-1]
        return short
        
