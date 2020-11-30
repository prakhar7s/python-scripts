#  Please write a program which count and print the numbers of each character in a
# string input by console.

inp_str = input("Enter string: ")
unique_chars = sorted(set(inp_str))
for ch in unique_chars:
    print(ch, inp_str.count(ch))

# using dictionary    
# inp_str = input("enter string: ")
# ans = {}
# for ch in inp_str:
#     ans[ch]=ans.get(ch,0)+1
# print(ans)
