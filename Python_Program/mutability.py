# Mutability & immutability
# Lists are mutable
# Tuples and Strings are immutable

s1 = "Python is fun"
s2 = s1.replace("Python", "Java")
print(s1)
print(s2)

t1 = ["Mango", "Orange", "Apple"]
print(id(t1))
t1.append("Pineapple")
print(t1)

l1 = ["Mango", "Orange", "Apple"]
l1[-1]= "Pineapple"
print(l1)

s1 ="Python is fun"
print(s1)
s1[0
] = 'p'
print(s1)