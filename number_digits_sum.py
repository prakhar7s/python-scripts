# WAP to input any number and display the sum of its each digit.
# Input: 6732 Output: 6+7+3+2 =18

n = int(input())
sum_of_digits = 0
while(n!=0):
    sum_of_digits+=(n%10)
    n//=10
print(sum_of_digits)

# one liner
# print(sum(map(lambda x: int(x), input())))
