class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(" ")
        res=[]
        for ele in s:
            if ele.strip():
                res.append(ele)

        return len(res[-1])
