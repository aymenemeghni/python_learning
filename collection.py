# collection = single variable that can store multiple values
# list = [] : ordered (indexable), mutable (changeable), allows duplicate values
# tuple = () : ordered (indexable), immutable (unchangeable), allows duplicate values , faster than list
# set = {} : unordered (not indexable), mutable (changeable), does not allow duplicate values
# dictionary = {} : ordered (indexable), mutable (changeable), allows duplicate values
#exemple:
#list:
my_list = [1, 2, 3, 4, 5, 5, 5]

dir(my_list) # show all methods and attributes of list
help(my_list) # show documentation of list 
len(my_list) # show number of items in list

# value in my_list # check if value is in list

print(my_list)
print(my_list[0]) # access value by index
print(my_list[0::2]) # syntax : list[start:stop:step]
# start = index to start from (defualt 0) [optional]
# stop = index to stop at (not included) (defualt last index) [optional]
# step = step size (defualt 1) [optional]

my_list.append(6) # add value to the end of the list
print(my_list)
my_list.remove(6) # remove value from the list
print(my_list)
my_list.insert(2, 10) # insert value at specific index
print(my_list)
my_list.pop(2) # remove value at specific index or last value if no index is given
print(my_list)
my_list.sort() # sort the list
print(my_list)
my_list.reverse() # reverse the list
print(my_list)
my_list.index(5) # get the index of value
print(my_list)
my_list.count(5) # count the number of value
print(my_list)
my_list.remove(5) # remove value from the list
print(my_list)

#tuple:
my_tuple = (1, 2, 3, 4, 5, 5, 5)
print(my_tuple)
my_tuple.count(5) # count the number of value
print(my_tuple)
my_tuple.index(5) # get the index of value
print(my_tuple)
my_tuple.remove(5) # remove value from the list
print(my_tuple)

#set:
my_set = {1, 2, 3, 4, 5, 5, 5}
print(my_set)
my_set.add(6) # add value to the set
print(my_set)
my_set.remove(6) # remove value from the set
print(my_set)
my_set.pop() # remove value from the set
print(my_set)
my_set.clear() # clear the set
print(my_set)
 
#dictionary:
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)
my_dict.get("name") # get value by key
print(my_dict)
my_dict.pop("name") # remove value by key
print(my_dict)
my_dict.update({"name": "John", "age": 30, "city": "New York"}) # update dictionary
print(my_dict)
my_dict.popitem() # remove last item
print(my_dict)
