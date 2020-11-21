# By using list comprehension, please write a program to print the list after
# removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

inp_list = [x for x in map(int, input("list: ").split())]
remove_index = [0,4,5]
rem_045 = [x for index, x in enumerate(inp_list) if index not in remove_index]
print(rem_045)
