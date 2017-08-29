
squares = {1:1, 2:4, 3:9, 4:16, 5:25}  
# remove a particular item
print(squares.pop(4))  
# Output: 16
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 5: 25}
# remove an arbitrary item
print(squares.popitem())
# Output: (1, 1)
print(squares)
# Output: {2: 4, 3: 9, 5: 25}
# delete a particular item
del squares[5]  
print(squares)
# Output: {2: 4, 3: 9}
# remove all items
squares.clear()
print(squares)
# Output: {}
# delete the dictionary itself
del squares
# Throws Error
# print(squares)
