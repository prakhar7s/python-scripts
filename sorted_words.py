# Write a code which accepts a sequence of words as input and prints the words in
# a sequence after sorting them alphabetically. Hint: In case of input data being
# supplied to the question, it should be assumed to be a console input.

inp_words = input("Enter words: ").split()
sorted_inp = sorted(inp_words)
print("Sorted sequence of words are: ", sorted_inp)
