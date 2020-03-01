import numpy as np
import sys

# sorting
print("----sorting-----")
a = np.array([[9, 6, 8], [4, 5, 1], [12, 2, 7]], np.int64)
print(a)
print(np.sort(a))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))  # it is same as simple sorting

dt = np.dtype([('name', 'S10'), ('age', int)])  # here S10 is no of character in the name and the age is in int.
a = np.array([('raju', 21), ('anil', 25), ('ravi', 17), ('amar', 27)], dtype=dt)

print('Our array is:')
print(a)
print('Order by name:')
print(np.sort(a, order='name'))
print(np.sort(a, order='age'))

# numpy.nonzero
print("----nonzero----")
a = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])

print('Our array is:')
print(a)

print('Applying nonzero() function:')
print(np.nonzero(a))  # check the indexes in output that is  for rows[0, 0, 1, 1, 2, 2], for col [0, 1, 1, 2, 0, 2]
print(a[np.nonzero(a)])
# np.where
print("-----np.where-----")
x = np.arange(9).reshape(3, 3)
print(x)
y = np.where(x > 3)
print(y)
print(x[y])

# extract() function returns the elements satifying any condition
print("----extract----")
x = np.arange(9).reshape(3, 3)
print(x)
condition = np.mod(x, 2) == 0
print(condition)
print(np.extract(condition, x))
print("or")
x = np.arange(9).reshape(3, 3)
print(x)
condition = np.add(x, 2)
print(condition)
print(np.extract(condition, x))

print("-------------")
a = np.arange(24)
print(a)
print(a.ndim)

# now reshape it
b = a.reshape(2, 4, 3)  # it means divide it into 2 diff matrix with (4 rows and 3 cols)
print(b)  # b is having three dimensions


# to convert datatype
print("------convert datatype-------")
rng = np.arange(99).reshape(33, 3)
print(rng.astype(float))
arr = rng.reshape(3, 33)
print(arr)
print(rng.astype(int))
a = rng.ravel()  # this is used to regain the original form
print(a)
print("--------line space---------")  # numpy.linspace(start, stop, num, endpoint, retstep, dtype)
lspace = np.linspace(1, 4, 6)
print(lspace)
lspace2 = np.linspace(1, 4, 6, endpoint=False)
print(lspace2)
lspace = np.linspace(1, 20, 10)  # the element is from 1 to 20 in 10 equal spacing
print(lspace)
# retstep
print("-------")
x = np.linspace(1, 2, 5, retstep=True)
print(x)

print("------power-------")
print(np.power(100, 5))
a = np.power(100, 5)
print(a.dtype)  # by default dtype is 32 bit and it is not good for long values it can show results for (10 power 5)

print(np.power(100, 5, dtype=np.int64))

# empty array
print("----empty----")
emp = np.empty((4, 6))  # it will bring us the empty array in which all the elements are random
print(emp)

emp = np.empty_like(lspace)  # this bring us the size of an array which we pass from it
print(emp)

# identity matrix
print("----iddentity---")
ide = np.identity(10)
print(ide)

print("-----NUMPY Axis-------")
# 2-d array
x = [[1, 2, 3], [4, 5, 6], [7, 1, 0]]
arr = np.array(x)
print(arr)
print("-------")
print(arr.sum(axis=0))  # sum of all coloumns
print(arr.sum(axis=1))  # sum of all rows
print("-------")
print(arr)
print(arr.argmax(axis=0))  # this will give us index of the max value on axis=0 all coloumns
print(arr.argmax(axis=1))  # this will give us index of the max value on axis=1 all rows
print("-------")
print(arr.T)  # this is the transpose of matrix

print(arr.flat)  # it shows the result in on vertical line
for item in arr.flat:
    print(item)
print("---------")
# they are attributes if we use .size() it will become function
print(arr.ndim)
print(arr.size)
print(arr.nbytes)  # how much space it covers
print("---------")

print("------1-D array-----")
arr = np.array([1, 2, 3, 4, 57, 9])
print(arr.argmax())  # this will give us the max element index = 4
print(arr.argmin())  # this will give us the min element index = 0
print(arr.argsort())  # this will give us the sorting of indexing of the elements

# importing sys which show size
py_ar = [0, 4, 55, 2]
np_ar = np.array(py_ar)
# this is size comparison b/w python array qnd numpy array
print(sys.getsizeof(1) * len(py_ar))
print(np_ar.itemsize * np_ar.size)

print("------Overflows errors-------")
# numpy provide the [numpy.iinfo and numpy.finfo] to verify the min or max value of numpy integers and float values resp
print(np.iinfo(np.int))
print(np.finfo(np.float))

# genfromtxt => it consists of 2 main loops
# 1)=> converts each line of the file in sequence of strings.
# 2)=> converts each strings to the apporiate data type.
print("-------import data from genfromtxt--------")
# import numpy as np
from io import StringIO

data1 = u"1h 2 3\n4 5 6"
# splitting the lines into columns
# the delimiter tells us how the splitting should take place
# the delimiter also include the spaces
data = np.genfromtxt(StringIO(data1), delimiter=2)
print(data)
print("----------")
data2 = u"  1  2  3\n  4  5 67\n890123  4"
data = np.genfromtxt(StringIO(data2), delimiter=3)
print(data)
print("------------")
data3 = u"123456789\n   4  75555 9\n   4567 9"
data = np.genfromtxt(StringIO(data3), delimiter=(4, 3, 2))
print(data)

print("----indexing----")
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a)
# slice items starting from index
print('Now we will slice the array from the index a[1:]')
print(a[1:])
print("-----numoy.nditer------")
'''NumPy package contains an iterator object numpy.nditer. It is an efficient multidimensional iterator object using 
which it is possible to iterate over an array. Each element of an array is visited using Python’s standard Iterator 
interface '''
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)

print('Original array is:')
print(a)

print('Modified array is:')
for x in np.nditer(a):
    if x > 25:
        print(x)

print("-----")
for x in np.nditer(a, order='C'):  # this order is for get the value in the form of row wise
    print(x)

# print("------")
# for x in np.nditer(a, order='F'):  # this order is for get the value in the form of coloumn wise
#     print(x)
#
# print("--op_flag is optional parameter for the nditer by default it is in read format----")
# print(a)
# for x in np.nditer(a, op_flags=['readwrite']):
#     x[...] = 2 * x
# print('Modified array is:')
# print(a)

# print("-----------")
# a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
#
# print('Our array is:')
# print(a)
#
# # this returns array of items in the second column and dots are always three
# print('The items in the second column are:')
# print(a[..., 1])
#
# # Now we will slice all items from the second row
# print('The items in the second row are:')
# print(a[1, ...])
#
# # Now we will slice all items from column 1 onwards
# print('The items column 1 onwards are:')
# print(a[..., 1:])
# print("-------------")


# x = np.arange(10)
# x.shape = (2, 5)
# print(x)
# print(x[0:2])
# print(x[1, -4])
# print(x[0:2])
# print("--------")
# y = np.arange(35).reshape(5, 7)
# print(y)
# print(y[1:5:2, ::3])  # print (y[row,coloumn]) we will first do independently then we will do jointly
# print("--------")
# print(y)
# # it means 0,0 and 2,1 and 4,2 of the y matrix
# #            rows                columns
# print(y[np.array([1, 1, 1, 2, 2, 2, 2]), np.array([4, 5, 6, 1, 2, 3, 4])])
# print("-------")
# print(y[np.array([0, 2, 4]), 1])
# print("-------")
# print(y[np.array([0, 2, 4]), 1:3])
#
# print("-----advance indexing------")
# z = np.arange(81).reshape(3, 3, 3, 3)
# print(z)
# print("---------")
# print(z[1, :, :, 2])
# print("--------")
# print(z[1, :, 2])
# print("---------")
# print(z[1, 2])
#
# # boolean or mask index array
# print("-----boollean array-------")
# b = y > 20
# print(b)
# print(y[b])
#
# print("-----to add a new axis-----")
# print(y.shape)
# print(y[:, np.newaxis, :].shape)
# print(y.shape)

# x, *y = {1: 2, 3: 4, 4: 5}
# print(*y)
# print(x)
