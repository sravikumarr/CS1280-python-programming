#Program 6(b)
#python program that creates 3 X 3 matrices between 1 and 10 . Perform amtrix suubtraction, element wise division , of both matrices
import numpy as np

matrix1 = np.random.randint(1, 11, (3, 3))
matrix2 = np.random.randint(1, 11, (3, 3))

print("Matrix 1:\n", matrix1)
print("\nMatrix 2:\n", matrix2)

sub = matrix1-matrix2
division= matrix1 / matrix2

print("\nMatrix Subtraction:\n", sub)
print("\nElement-wise Division:\n", division)
