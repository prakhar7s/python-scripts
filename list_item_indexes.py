# Write a for loop that prints all elements of a list and their position in the list.a =
# [4,7,3,2,5,9] 


inp_list = [x for x in map(int, input().split())]
for index, x in enumerate(inp_list):
    print("{0} is at {1}".format(x, index+1))
