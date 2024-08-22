# All Numpy Functions
import numpy as np

# np.empty - This function creates an array of specified length and datatype with some random values
print("Empty array")
print(np.empty(2, dtype=int))
print(np.empty([2,2], dtype = float))

#np.zeros
print("Zero Array")
print(np.zeros(2,dtype = int))

# np.arange([start], stop) this function prints the range of numbers starting from 0 t0 num - 1
print(np.arange(5))

# np.reshape - Reshapes an array
print("Reshape array")
print(np.arange(8).reshape(2,4))

# flatten - use this method to copy the array collapsed into one dimension
print("Flattened Array")
print(np.array([[1,2,3],[4,5,6],[7,8,9]]).flatten())
print(np.array([[1,2,3],[4,5,6],[7,8,9]]).flatten('F'))  #column major order

# np.append/np.concatenate - Appends valuesat the end of the array
print("Append Array")
arr = np.array([1,2,3,4])
print(np.append(arr, [5,7,8]))


# hstack() and vstack()
arr1 = np.array([[1,2,3],[-1,-2,-3]])
arr2 = np.array([[4,5,6],[-4,-5,-6]])

print(np.hstack((arr1,arr2)))
print(np.vstack((arr1,arr2)))

# empty()      	                Return a new array of given shape and type, without initializing entries
# empty_like()	        Return a new array with the same shape and type as a given array
# eye()	Return           a 2-D array with ones on the diagonal and zeros elsewhere.
# identity()   	        Return the identity array
# ones()	            Return a new array of given shape and type, filled with ones
# ones_like()	        Return an array of ones with the same shape and type as a given array
# zeros()   	        Return a new array of given shape and type, filled with zeros
# zeros_like()	        Return an array of zeros with the same shape and type as a given array
# full_like()	        Return a full array with the same shape and type as a given array.
# array()	            Create an array
# asarray()         	Convert the input to an array
# asanyarray()         	Convert the input to an ndarray, but pass ndarray subclasses through
# ascontiguousarray()	Return a contiguous array in memory (C order)
# asmatrix()	        Interpret the input as a matrix
# copy()	            Return an array copy of the given object
# frombuffer()	        Interpret a buffer as a 1-dimensional array
# fromfile()	        Construct an array from data in a text or binary file
# fromfunction()	    Construct an array by executing a function over each coordinate
# fromiter()	        Create a new 1-dimensional array from an iterable object
# fromstring()	        A new 1-D array initialized from text data in a string
# loadtxt()	            Load data from a text file
# arange()	            Return evenly spaced values within a given interval
# linspace()	        Return evenly spaced numbers over a specified interval
# logspace()	        Return numbers spaced evenly on a log scale
# geomspace()	        Return numbers spaced evenly on a log scale (a geometric progression)
# meshgrid()	        Return coordinate matrices from coordinate vectors
# mgrid()	            nd_grid instance which returns a dense multi-dimensional “meshgrid
# ogrid()	            nd_grid instance which returns an open multi-dimensional “meshgrid
# diag()	            Extract a diagonal or construct a diagonal array