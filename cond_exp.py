#conditional expressions 
# syntax = (value_if_true) if (condition) else (value_if_false)

from datetime import date
age = 18
print("Eligible" if age >= 18 else "Not Eligible")

# another example

num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

year = 2027 if date.today().year % 4 == 0 else date.today().year
print("Leap year" if year % 4 == 0 else "Not a leap year")