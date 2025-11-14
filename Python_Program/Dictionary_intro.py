# comma separated key-value pairs enclosed within {}
# {key1: value1, key:value2, ............}

groceries = {'milk': 60, 'biscuits': 20, 'rice': 90, 'break': 30}
print(groceries)
# print(type(groceries))
# print(len(groceries))

print(groceries['milk'])

groceries['rice'] = 140
print(groceries)

groceries['egg'] = 10 # add new key-value pair to the dictionary groceries
groceries['bread'] = 35 # updates the value of the key
print(groceries)