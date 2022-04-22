from unittest import result
import math

def PalindromeChecker(x):
    return False if x < 0 else x == int(str(x)[::-1])

print(PalindromeChecker(655))