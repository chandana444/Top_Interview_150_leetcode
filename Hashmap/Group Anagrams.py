class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1=defaultdict(list)
        for i in strs:
            key="".join(sorted(i))
            map1[key].append(i)
        return list(map1.values())

