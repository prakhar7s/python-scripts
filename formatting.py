import math

num = 3.5422

print(math.trunc(num))  # integral part
print(math.ceil(num))  # smallest number in int which is greater than this number
print(math.floor(num))  # greatest int which is smaller than this number

# setting precision of floating-point values

a = 23

# using % operator similar to printf
print('%.4f' % a)

# format()
print("{0:.4f}".format(a))

# round()
print(round(a, 1))
