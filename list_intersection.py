# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a 
# program to make a list whose elements are intersection of the above given list

list1 = [x for x in map(int, input("list1: ").split())]
list2 = [x for x in map(int, input("list2: ").split())]

intersct_list = []

for x in set(list1):
    if x in list2:
        intersct_list.append(x)

print(intersct_list)
