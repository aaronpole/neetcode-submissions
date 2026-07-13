class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        r_count = {}
        for i in s:
            s_count[i] = s_count.get(i,0)+1
        for i in t:
            r_count[i] = r_count.get(i,0)+1
        if s_count == r_count:
            return True
        return False