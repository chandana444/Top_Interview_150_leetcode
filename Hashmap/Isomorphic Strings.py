from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
#method1
        """i,sc,tc=0,0,0
        while i<len(s):
            for j in range(s.count(s[i])):
                sc+=s.index(s[i])
                tc+=t.index(t[i])
                if(sc==tc):
                    i+=1
                else:
                    return False
        return True  #less space complexity method or"""
#method2
        map1=[]
        map2=[]
        for i in s:
            map1.append(s.index(i))
        for i in t:
            map2.append(t.index(i))
        if map1==map2:
            return True
        return False
        
