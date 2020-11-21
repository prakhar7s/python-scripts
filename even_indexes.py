#  Please write a program which accepts a string from console and print the 
# characters that have even indexes.

# PRAKHAR SHRIVASTAVA 0225CS181030

inp_str = input("enter string: ")
str_len = len(inp_str)
for x in range(0, str_len, 2):
    print(inp_str[x], end=" ")
    
