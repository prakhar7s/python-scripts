# Write a program that accepts a sentence and calculate the number of letters and
# digits. 
# Suppose if the entered string is: Python0325Then the output will be: LETTERS: 6 
# DIGITS:4. Hint: Use built-in functions of string.

inp = input("Enter sentence: ")
digits_count = 0
letters_count = 0
for ch in inp:
    ch_ascii = ord(ch)
    if(ch_ascii>=48 and ch_ascii<=57):
        digits_count+=1
    elif((ch_ascii>=65 and ch_ascii<=87) or (ch_ascii>=97 and ch_ascii<=122)):
        letters_count+=1

print("LETTERS:", letters_count)
print("DIGITS:",digits_count)
