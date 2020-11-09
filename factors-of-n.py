# O(sqrt(n)) solution of finding the factors of a number

import math

def factors_of_n(n):
    sqrt_n = math.sqrt(n)
    x = 1
    while x<=sqrt_n:
        if not n%x:
            print(x)
            if not x==n//x:
                print(n//x)
        x+=1
        
factors_of_n(int(input("n: ")))
