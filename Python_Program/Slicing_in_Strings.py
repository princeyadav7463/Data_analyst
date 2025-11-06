s1 = "Hello world"
print(s1)

#length of the string
print(len(s1))

#Indexing
print("First char", s1[0])
print("Last char", s1[-1])

"""
syntax of indexing : start[index]
syntax of slicing : string[start:end:step]
- Start : starting index at which the slicing operation starts
- end : ending index at which the slicing stops (excluded)
- step : integer that specifies the step for the slicing 
"""
#print(s1[2:7:1])
#print(s1[2:9:2])
print(s1[1:12:3])