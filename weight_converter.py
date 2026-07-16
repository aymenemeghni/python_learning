# Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Enter the unit of weight (lbs or kg): ")

if unit == "lbs":
    weight = weight * 0.453592
    print("Your weight in kg is: ", weight)
elif unit == "kg":
    weight = weight * 2.20462
    print("Your weight in lbs is: ", weight)
else:
    print("Invalid unit")




