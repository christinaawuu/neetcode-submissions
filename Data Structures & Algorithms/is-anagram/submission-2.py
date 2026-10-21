class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        
        
        sString = list(s)

        for j in t:
            if j in sString:
                sString.remove(j)

        if not sString:
            return True

        return False