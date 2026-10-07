import random 
# random numbers are used to generate random numbers 

#print(help(random))  # show documentation of random module 
#print(dir(random))  # show all methods and attributes of random module 

computer = random.randint(1,100) #random integer between 1 and 100
random.choice(["a","b","c"])  #random choice from list 
random.choices(["a","b","c"]) #random choice from list 
random.shuffle(["a","b","c"]) #random shuffle of list
list1 = ["a","b","c"]
print(list1)
random.shuffle(list1)
print(list1)
random.uniform(1,100) #random float between 1 and 100
number = random.random() #random float between 0 and 1

print(computer)
player = int(input("Enter your choice (between 1 and 100): ")) #player choice
if player <1 and player >100:
    print("Invalid choice") #invalid choice 

print(player) #player choice

if player > computer:
    print("You win")
elif player < computer:
    print("Computer wins")
else:
    print("It's a tie") 
    