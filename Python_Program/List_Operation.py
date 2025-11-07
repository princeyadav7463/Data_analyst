
"""
# Slicing of Lists
l1 = [3, 8, 6, 9, 0, 6, 9, 7, 6]
print(l1[1:6:1])
print(l1[2:6:2])

# Concatenation of lists
l1 = [1, 7, 2]
l2 = [0,5]
print(l1 +l2)

# Repetition of lists
l1 = [1, 7, 2]
l2 = [0,5]

print(l2 * 3)

# Append()
# Adds an item to the end of the list

fruits = ["apple", "banana", "cherry"]
print(fruits)
# syntax: list.append(item)
print(fruits.append("Grape"))
print(fruits)

s1 = "python is fun"
print(s1.replace("python", "Java"))

# insert
# adds an element before the specified index
# syntax: list.insert(index, item)
fruits.insert(2,"Papaya")
print(fruits)

"""
from Fstring_python import language
from List_in_Python import days_of_week

'''
extend()
remove()
pop()
reverse()
sort()
'''
# extend
fruits = ["Apple", "Banana", "Orange"]
fruits.extend(["Mango", "Grapes"])
print(fruits)

# remove()
fruits_name = ["Apple", "Banana", "Orange"]
print(fruits_name)
fruits_name.remove("Banana")
print(fruits_name)

# pop
vegetables_name = ["cucumber", "chilli", "lady finger", "cauliflower", "carrot"]
print(vegetables_name)
vegetables_name.pop(2)
print(vegetables_name)

# reverse
vegetables_name = ["cucumber", "chilli", "lady finger", "cauliflower", "carrot"]
print(vegetables_name)
vegetables_name.reverse()
print(vegetables_name)

# sort
vegetables_name = ["cucumber", "chilli", "lady finger", "cauliflower", "carrot"]
print(vegetables_name)
vegetables_name.sort()
print(vegetables_name)

# count

numbers = [6,2, 2, 6, 7, 0,3, 2, 7, 22, 33, 0, 12, 11, 6, 0, 88, 45, 0, 20, 10, 62, 0, 85]
print(f"The list is: {numbers}")
item_to_count = int(input("Enter the number to be counted from the above list:"))
c = numbers.count(item_to_count)
print(f"Occurrence of {item_to_count} is {c}")

# in
language = ["Python", "java", "c", "c++", "html", "css"]
print("Python" in language)