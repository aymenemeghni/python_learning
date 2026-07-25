#format specifiers {value:flags}
#flags are 
# .2f - format as a float with 2 decimal places
# 10 - width of the field
# 0 - fill with zeros
# ^ - center alignment
# < - left alignment
# > - right alignment
# + - show the sign
# - - show the sign
# ' ' - show the sign
# , - show the sign
# : - show the sign


price1=1.23456
price2=2.23456
price3=3.23456

print(f"${price1:10.2f}")
print(f"${price2:10.2f}")
print(f"${price3:10.2f}")

