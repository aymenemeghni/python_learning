import random 
# random numbers are used to generate random numbers 

#print(help(random))  # show documentation of random module 
#print(dir(random))  # show all methods and attributes of random module 

computer = random.randint(1,100)
print(computer) #random integer between 1 and 100
player = int(input("Enter your choice (between 1 and 100): "))
if player <1 and player >100:
    print("Invalid choice") 

print(player) #player choice

if player > computer:
    print("You win")
elif player < computer:
    print("Computer wins")
else:
    print("It's a tie") 
    
