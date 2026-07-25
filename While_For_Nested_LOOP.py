# While_For_Nested_LOOP.py

# While loop : excute some code while a condition is true 
# while [condition]:
#     statement(s)
#exemple
name = input("Enter your name: ").strip()
while name != "":
    print("Hello ", name)
    name = input("Enter your name: ").strip()

# For loop : excute some code for a fixed number of times
# first syntax:
# for [variable] in range([start],[stop],[step]):
#     statement(s)
# second syntax:
# for [variable] in reversed(range([start],[stop],[step])):
#      statement(s)
# start is optional and default is 0 (inclusive)
# stop is optional and default is 0 (exclusive)
# step is optional and default is 1 
#example:

for i in range(10):
    print(i)

# Nested loop : one loop inside another loop 
# for [variable] in [sequence]:
#     for [variable] in [sequence]:
#         statement(s)

# example 
