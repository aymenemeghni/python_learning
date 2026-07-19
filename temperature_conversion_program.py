# Temperature Conversion Program
unit = input("Enter the unit of temperature in celcius (C) or fahrenheit (F): ")
temperature = float(input("Enter the temperature: "))

if unit == "C":
    temperature = (temperature * 9/5) + 32
    print(f"Your temperature in fahrenheit is: {temperature} °F")
elif unit == "F":
    temperature = (temperature - 32) * 5/9
    print(f"Your temperature in celcius is: {temperature} °C")
else:
    print("Invalid unit")