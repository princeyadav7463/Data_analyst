# Sets are non-sequential collection of items
# comma separated element enclosed within {}
# Sets do not allow duplicate elements


set1 = {10, "Python", 2.5}
print(set1)
print(type(set1))

# Length of the set
print(len(set1))

l1 = [10, 2.5, 30, 10,30,10]
print(l1, type(l1))
s1 = {10, 2.5, 30, 10,30,10}
print(s1, type(s1))

# Are sets mutable or immutable?
set1 = {2, 0, -1}
print(set1)
# add
set1.add(6)
print(set1)

# remove
set1.remove(6)
print(set1)

# add duplicate number 0
set1.add(0)
print(set1)

# discard () using for removing element without error
set1.discard(2)
print(set1)
