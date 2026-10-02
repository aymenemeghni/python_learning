# dictionary: key-value pairs {"key":"value"}
# ordered data and not allow duplicates data and changeable data
# duplicate key will be ignored

capitals = {"algeria":"algiers","france":"paris","spain":"madrid","usa":"washington d.c."}

print(dir(capitals))  # print all methods of dictionary

print(capitals)   # print dictionary in order
print(capitals.keys())  # print keys only
print(capitals.values())  # print values only
print(capitals.items())  # print key-value pairs
print(capitals.get("algeria"))  # print value of key "algeria" , return false if not existe
print(capitals.update({"usa":"new york"}))  # update value of key "usa"
print(capitals.pop("usa"))  # remove key "usa"
print(capitals.popitem())  # remove last key-value pair
print(capitals.clear())  # remove all key-value pairs



