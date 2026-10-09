# functions = a block of code that performs a specific task
# execute once , use many times when i called 

# syntax = " def function_name(): " or " lambda arguments : expression " 
# "def" keyword is used to define a function 
# "lambda" keyword is used to define a anonymous function 
# syntax = "(function_name())" or "(lambda arguments : expression)()"

# syntax function with parameters 
# def function_name(param1, param2, ...):
#    """ docstring """
#    function body
#    return expression


# types of functions: 
# 1. Built-in functions 
# 2. User-defined functions 
# 3. Recursive functions 
# 4. Higher-order functions 
# 5. Nested functions 

# default arguments : a value that is assigned to a parameter in the function definition
# the default value is use if no value is passed to the parameter
def add(a, b = 20):
   return a + b
print(add(10))

# keyword arguments : arguments that are passed to the function in the form of keyword arguments
# an argument preceded by a keyword, name is always precede by ** when it is used as a parameter
# order doesn't matter in keyword arguments
def add(a, b):
   return a + b
print(add(a = 10, b = 20))
print(add(b = 20, a = 10))

#arbitrary arguments : arguments that are passed to the function in the form of arbitrary arguments
# an argument preceded by a * when it is used as a parameter
# the number of arguments can be anything
#the arguments are stored in a tuple
def add(*args):
   return sum(args)
print(add(10, 20, 30, 40, 50))

#arbitrary keyword arguments : arguments that are passed to the function in the form of arbitrary keyword arguments
def add(**kwargs):
   return sum(kwargs.values())
print(add(a = 10, b = 20, c = 30, d = 40, e = 50))

# example of user defined function  with no parameters
def say_hello():
    print("Hello! This is a simple function.")
say_hello()

# example of user defined function with parameters:
def add(a, b):
   return a + b
print("the sum of two numbers is:", add(10, 20) )

   



