# string indexing is used to access the characters of a string
# string slicing is used to access a range of characters of a string
# string slicing is done using the syntax [start:stop:step]
# start is the starting index (inclusive)
# stop is the ending index (exclusive)
# step is the number of characters to skip (positive for forward, negative for backward)
# if start or stop is not given, it is assumed to be the beginning or end of the string respectively
# if step is not given, it is assumed to be 1


name = input("Enter your name: ")


print(name[-1]) # last character
print(name[-2]) # second last character
print(name[-3]) # third last character
print(name[::]) # all characters
