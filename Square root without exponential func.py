#https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        substract = 1
        counter = 0
        while x > 0:
            x = x - substract
            substract += 2
            if x < 0: break #Break karena diminta pembulatan kebawah, sqrt(8) ~ 2.82, harus return angka 2
            counter += 1
        return counter
    print(mySqrt(0,8))

