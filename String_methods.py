#string methods are used to manipulate strings 
#.lower(), .upper(), .capitalize(), .title(), .strip(), .split(), .replace()
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
# len() method is used to find the length of a string 


name =input("Enter your name: ").strip()
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title())
print(name.split())
print(name.replace(" ", "_"))
