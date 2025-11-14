# concatenation, repetition, membership, count, index, min, max, sum
student_detail1 = (1001, "John")
student_detail2 = (78.5, 91.0, 58.0, 52.8)
#  concatenation (+)
student_detail1 = student_detail1 + student_detail2
print(student_detail1)

# repetition (*)

t1 = ("Class 5", 8000)
print(t1 * 5)

# membership (in, not in)

print(91.0 in student_detail2)
print(83.0 not in student_detail2)
print(58.0 not in student_detail2)

# count ()
t4 = (10, 20, 30, 80, 90, 1, 90, 80, 90, 10, 20, 90)
# tuple.count(element)
print(t4.count(90))

# index()
t4 = (10, 20, 30, 80, 90, 1, 90, 80, 90, 10, 20, 90)
print(t4.index(80)) # what is the index of 80 in tuple t4

# min(tuple)
# max(tuple)
# sum(tuple)
print(f"Smallest number : {min(t4)}")
print(f"Largest number : {max(t4)}")
print(f"Total sum : {sum(t4)}")
