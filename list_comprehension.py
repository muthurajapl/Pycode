squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print (squares) # [1, 4, 9, 16, 25]

squares = []
for x in [1, 2, 3, 4, 5]: # This is what a list comprehension does
    squares.append(x ** 2) # Both run the iteration protocol internally
print (squares) # [1, 4, 9, 16, 25]