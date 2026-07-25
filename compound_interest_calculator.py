#compound interest calculator

principal =0
rate =0
time =0


while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal amount must be greater than 0")
        continue

while rate <= 0 or rate >= 100:
    rate = float(input("Enter the annual interest rate: "))
    if rate <= 0 or rate >= 100:
        print("Interest rate must be between 0 and 100")
        continue

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than 0")
        continue


compound_interest = principal * (1 + rate / 100) ** time
print("The compound interest is: ", compound_interest)    