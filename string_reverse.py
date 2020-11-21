# Please write a program which accepts a string from console and print it in reverse
# order.

inp_str = input("enter string: ")
reversed_str = "".join(reversed(inp_str))
# OR
reversed_str = inp_str[::-1] 
print("reversed string:", reversed_str)
