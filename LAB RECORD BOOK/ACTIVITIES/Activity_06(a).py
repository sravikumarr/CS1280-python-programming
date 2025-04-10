#Program 6 (a)
#Python program to create 3 X 3 Numpy array filled with random integer between 1 and 20, calculates the mean , and replaces all element less than 10 with 0
import numpy as np

array=np.random.randint(1,21, (3,3))
print("\nArray without the mean value : \n", array)
mean = np.mean(array)
print("\nArray with mean value : \n", mean)
array[array < 10 ] = 0
print("\nArray after replacing the value : \n ", array)
