from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine and (ransomNote.count(ransomNote[i])<=magazine.count(ransomNote[i])):
                continue
            else:
                return False
        return True
