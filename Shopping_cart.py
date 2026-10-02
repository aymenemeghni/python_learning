# shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food} DZD: "))
        foods.append(food)
        prices.append(price)
        
print("----Your Cart----\n")
for food in foods:
    print(food,end=", ") # end=" " : change the default end of line "\n" to " , " so the items are printed in the same line separated by " , "
print("\n")
for price in prices:
    print(f"{price} DZD",end=" , ")

total = sum(prices)

print(f"\nTotal price: {total} DZD")



