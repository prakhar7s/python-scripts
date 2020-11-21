# Write a program which will find factors of given number and find whether the factor
# is even or odd. Hint: Use Loop with if-else statements

import math

def factors(n):
    factors_n = []
    sqrt_n = math.sqrt(n)
    i = 1
    
    while i<=sqrt_n:
        if n%i==0:
            if n//i==i:
                factors_n.append(i)
            else:
                factors_n.append(i)
                factors_n.append(n//i)
        i+=1
    
    return sorted(factors_n)

def even_or_odd(factors):
    even_factors = []
    odd_factors = []
    for x in factors:
        if x%2:
            odd_factors.append(x)
        else:
            even_factors.append(x)
    return [sorted(even_factors), sorted(odd_factors)]

n=int(input("Enter any natural number: "))
factors_n = factors(n)
print("All factors of n: ",*factors_n)
even_factors, odd_factors = even_or_odd(factors_n)
print("Even factors: ", *even_factors)
