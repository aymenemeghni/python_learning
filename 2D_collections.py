# 2d collections

fruits = ["apple","banana","cherry"]
vegetables = ["potato","carrot","onion"]
meats = ["beef","chicken","fish"]

groceries = [fruits,vegetables,meats]

print(groceries)
print(groceries[0])
print(groceries[0][0]) 
# print (groceries[i][j] where i is the index of the list
# and j is the index of the item in the list)


for i in groceries:
    for j in i:
        print(j , end=" ")
    print()