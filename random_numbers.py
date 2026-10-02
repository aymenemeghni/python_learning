# random numbers are used to generate random numbers 

import random 
print(help(random))  # show documentation of random module 
print(dir(random))  # show all methods and attributes of random module 

computer = random.randint(1, 3)
print(computer)
