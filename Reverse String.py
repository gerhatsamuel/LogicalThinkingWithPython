class Solution:
    def reverseString(self, s: list[str]) -> None:
        x = 0
        y = len(s)-1
        while x < y:
            s[x],s[y]= s[y],s[x]
            x += 1
            y -= 1
        return s
    Input = ["N","I","C","E"]
    print(reverseString(1,Input))