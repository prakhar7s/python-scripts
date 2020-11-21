# By using list comprehension, please write a program to print the list after
# removing delete numbers which are divisible by 5 and 7 in 

import ast
inp_list = ast.literal_eval(input("list:"))
inp_list = [x for x in inp_list if all([(x%5), (x%7)])]
print("Numbers which are not divisible by 5 or 7: ",inp_list)
