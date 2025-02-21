# Create a dictionary with numbers and their squares
squares = {x: x*x for x in range(6)}
print(squares) 
# Dictionary with squares of odd numbers
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(odd_squares) 
