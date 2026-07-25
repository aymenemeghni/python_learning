#just learning python 

from ast import keyword
first_name = "aymene"
food = "banana"
email = "meghnimohamedaymene@gmail.com"

print("your name is",first_name)

# "f" before the string used to format the string 

print(f"your name is {first_name}")
print(f"your favorite food is {food}")
print(f"your name is {first_name} and your favorite food is {food}")

#type casting "int()","float()","str()","bool()"" change the value from one type to another

#type() used to check the type of the value

print(type(food)) 

#input() used to get input from the user "input() always return a string" 

age = input("How old are you?: ")

print(f"you are {age} years old")

#keyword
#break :used to exit a loop
#continue :used to skip an iteration
#pass :used to do nothing
#return :used to return a value
#yield :used to return a generator
