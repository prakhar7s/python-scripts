#  Design a code which will find the given number is Palindrome number or not. Hint:
# Use built-in functions of string.

inp_str = input()
reverse_str = inp_str[::-1]
if inp_str == reverse_str:
    print("Palindrome")
else:
    print("Not Palindrome")
