class Solution:
    def romanToInt(self, s: str) -> int:
        Ans = 0
        Translation = {"I":1, "V":5, "X":10, "L":50, "C":100, "D": 500, "M":1000}
        for i in range(0,len(s)-1):
            if Translation[s[i]] < Translation[s[i+1]]:
                Ans = Ans - Translation[s[i]]
            else: 
                Ans = Ans + Translation[s[i]]
        return Ans + Translation[s[-1]]
