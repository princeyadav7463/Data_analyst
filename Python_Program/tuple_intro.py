"""
# tuple
# (item1, item2, .........)
# Sequence of items as a collection
t1 = ("Python", 10, 1.5, True, (1,2,3),(10, 20))
print(len(t1))

# Accessing items of a tuple index
print(t1[0])
print(t1[-1])
"""
l1 = [1, 2, 3]
print(l1)
print(type(l1))

t1 = tuple(l1)
print(t1, type(t1))

fruits = ("Mango", "Orange", "Apple")
print(fruits, type(fruits))
fruits = list(fruits)
print(fruits)