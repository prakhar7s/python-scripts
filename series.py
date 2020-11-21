# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by
# console 

n = int(input())
ans = 0
for x in range(1,n+1):
    ans+=(x/(x+1))
print(ans)

# one liner
# sum([x for x in map(lambda x: x/(x+1), range(1, int(input())+1))])
