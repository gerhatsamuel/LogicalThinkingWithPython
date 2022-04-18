def FunctionSwap(a,b):
    a = a * b     # a = 35
    b = a / b     # b = 5
    a = a / b     # a = 7
    return a,b

print(FunctionSwap(5,7))