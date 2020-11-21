#  Write a program, which will find all the numbers between 1000 and 3000 (both
# included) such that each digit of a number is an even number. The numbers
# obtained should be printed in a comma separated sequence on a single line. Hint: In
# case of input data being supplied to the question, it should be assumed to be a
# console input. Divide each digit with 2 and verify is it even or not.

def all_digits_even(n):
    while( n!=0):
        x = n % 10
        if x % 2:
            return False
        n//=10
    return True 
        
for x in range(1000, 3001):
    if all_digits_even(x):
        print(x, end=" ")
