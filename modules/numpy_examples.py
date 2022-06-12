
# pip install numpy
import numpy as np


# Example #1
# Creating numpy array in python
# Create a rank 1 array
a = np.array([1, 2, 3])
print(type(a))            # Prints "<class 'numpy.ndarray'>"

print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"


a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"
#
# # Create a rank 2 array
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

print(b[1, 2])  # 6

# print("************* array index *******************")
# # Example #2:
# # Array indexing:
# """
# Numpy offers several ways to index into arrays.
#
# Slicing: Similar to Python lists, numpy arrays can be sliced.
#  Since arrays may be multidimensional,
# you must specify a slice for each dimension of the array:
# """
# import numpy as np
#
# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
#
# # Use slicing to pull out the subarray consisting of the first 2 rows
# # and columns 1 and 2; b is the following array of shape (2, 2):
# # [[2 3]
# #  [6 7]]
b = a[:2, 1:3]

# [
#     [1,2,3,4],
#     [5,6,7,8]
# ]

# [[2,3],
#  [6,7]]
print(b)
print(" KIRAN     *******************")
#
# # A slice of an array is a view into the same data, so modifying it
# # will modify the original array.
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77"
print(a)
print(a[0, 3])
#
#
print("*************** array boolean index *******************")
#
#
# #Boolean array indexing:
# """
# Boolean array indexing lets you pick out arbitrary elements of an array.
# Frequently this type of indexing is
# used to select the elements of an array that satisfy some condition.
# Here is an example:
# """
#
# import numpy as np
#
a = np.array([[1, 2], [3, 4], [5, 6]])
#
bool_idx = (a > 2)   # Find the elements of a that are bigger than 2;
#                      # this returns a numpy array of Booleans of the same
#                      # shape as a, where each slot of bool_idx tells
#                      # whether that element of a is > 2.
#
print(bool_idx)      # Prints "[[False False]
#                      #          [ True  True]
#                      #          [ True  True]]"
#
# #We use boolean array indexing to construct a rank 1 array
# # consisting of the elements of a corresponding to the True values
# # of bool_idx
print(a[bool_idx])  # Prints "[3 4 5 6]"
#
# # We can do all of the above in a single concise statement:
print(a[a > 2])     # Prints "[3 4 5 6]"
#
#
print("***************** numpy sum output **********")
# #Numpy provides many useful functions
# #for performing computations on arrays; one of the most useful is sum:
# import numpy as np
#
x = np.array([[1,2],
              [3,4]])
print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"