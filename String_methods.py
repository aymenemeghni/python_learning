#string methods are used to manipulate strings 
# .lower() method is used to convert a string to lowercase
# .upper() method is used to convert a string to uppercase
# .find() method is used to find the index of a first occurrence of a substring
# .rfind() method is used to find the index of a last occurrence of a substring
# .replace() method is used to replace all occurrences of a substring with another substring 
# .count() method is used to count the number of occurrences of a substring 
# .strip() method is used to remove leading and trailing whitespaces
# .lstrip() method is used to remove leading whitespaces
# .rstrip() method is used to remove trailing whitespaces
# .split() method is used to split a string into a list of substrings
# .join() method is used to join a list of substrings into a string
# .index() method is used to find the index of a substring
# .capitalize() method is used to capitalize the first letter of a string
# .title() method is used to capitalize the first letter of each word in a string
# .swapcase() method is used to swap the case of each letter in a string
# .isdigit() method is used to check if a string is a digit (only integers)
# .isdecimal() method is used to check if a string is a decimal (integers and decimals with a single decimal point)
# .isalpha() method is used to check if a string is a letter
# .isalnum() method is used to check if a string is a letter or a digit
# .islower() method is used to check if a string is a lowercase
# .isupper() method is used to check if a string is an uppercase
# .isspace() method is used to check if a string is a space
# .startswith() method is used to check if a string starts with a specific substring
# .endswith() method is used to check if a string ends with a specific substring
# len() method is used to find the length of a string 


name =input("Enter your name: ").strip()
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title())
print(name.split())
print(name.replace(" ", "_"))
