#logical operations = and, or, not 

temp = 25
is_rainy = False 
is_sunny = True

if temp > 30 and is_sunny:
    print("It's hot and sunny")
elif temp > 30 and is_rainy:
    print("It's hot and rainy") 
elif temp > 30 or is_rainy:
    print("It's hot or rainy")
else:
    print("It's neither hot nor rainy") 

