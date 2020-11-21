# WAP for multiplication table generation.

n = int(input())
for x in range(1, 11):
    print("{0} x {1} = {2}".format(n, x, n*x))
