from unittest import result
import math

def PalindromeChecker(x):
    return False if x < 0 else x == int(str(x)[::-1])

print(PalindromeChecker(555))



"""
def NumberChecker(x):
    if x % 2 == 1:
        return "Even"
    else : return "Odd"

print(NumberChecker(0))
print(NumberChecker(1))
"""

"""
def FunctionSwap(a,b):
    a = a * b     # a = 35
    b = a / b     # b = 5
    a = a / b     # a = 7
    return a,b

print(FunctionSwap(5,7))
"""