from Fstring_python import language

s1 = "python is fun"
print(s1[0])
print(s1[-1])
print(len(s1))


language = "Python"
version = " 3.13.3"
print(language + version)

print("Python" + "P")

print(s1 * 3)

#In string, '*' is repetition operator

#Membership operation
# in operator we check given character is available or not

print("Python" in s1)
print("i" in s1)
print("z" in s1)
print("java" in s1)


#not in
print("z" not in s1)
print("java" not in s1)
print("Python" not in s1)
print(s1)

#comparison of strings
print("Python " == "Python")


#  Removing spaces from a string - strip()

s1 = "   Python     "
print(s1.strip() == "Python")
print(s1.lstrip() == "Python")
print(s1.rstrip() == "Python")

#replace()
s1 = "we are learning Python"
print(s1)
print(s1.replace("Python", "Java"))
print(s1)

# counting substring from a string
#count()
# String.count(substring)
s1 = "We are learning Python. Python is fun."
s2 = "python"
print(s1.count(s2))

print(f"Occurrences of {s2} is {s1.count(s2)}")

#Changing case of a sting
#upper(), lower(), title(), capatilize()

s1 = "We are learning Python"
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.capitalize())


# startswith()
# string.startswith(substring)

print(s1.startswith("We"))

# endswith()
print(s1.endswith("Python"))