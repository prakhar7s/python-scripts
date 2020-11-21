# By using list comprehension, please write a program to print the list after
# removing the value 24 in [12,24,35,24,88,120,155].

inp_list = [x for x in map(int, input("list: ").split())]
rem_24 = [x for x in inp_list if x != 24]
print(rem_24)


remove_element.py 
