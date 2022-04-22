#https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        length = len(digits)-1
        digits[length] = int(digits[length])+1
        if digits[length] >=10:
            depan = int(digits[length]/10)
            belakang = digits[length]%10
            digits = digits[:length]
            digits.append(depan)
            digits.append(belakang)
        return digits

    input1 = [1,2,3]
    input2 = [4,3,2,1]
    input3 = [9]

    print (plusOne(True,input1))
    print (plusOne(True,input2))
    print (plusOne(True,input3))    