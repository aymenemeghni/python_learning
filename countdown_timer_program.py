# countdown timer program

import time

#all methods in time module
# help(time) : show all methods in time module

my_time = int(input("Enter the time in seconds: "))
print(my_time)

time.sleep(my_time)  #pause the program for my_time seconds  
print(time.time())


my_time1 = int(input("Enter the time in seconds: "))
print(my_time1)

seconds = my_time1
minutes = seconds // 60
hours = minutes // 60
days = hours // 24
weeks = days // 7
months = days // 30
years = days // 365


print(f"{years}:{months}:{days}:{hours}:{minutes}:{seconds}")

