import numpy as np 
import sys
import time

'''Numpy most usefull feature is N-dimentional array object 
3 Benefits of numpy array over pytthon list
    1) Less memory (continous memory allocation but in python list every element is pointed to memory location using pointers)
    2) fast
    3)convinient'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                   Basic array operations
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# memory difference list vs numpy
l=range(1000)
print(l)

print("python list memory size in bytes",sys.getsizeof(1)*len(l))

array=np.arange(1000)
print("numpy array memory size in bytes",array.size*array.itemsize)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#python vs numpy access to memory(time )
size=1000000
l1=range(size)
l2=range(size)
a1=np.arange(size)
a2=np.arange(size)
#python list
start=time.time()
result=[(x+y for x,y in zip(l1,l2))]
print("numpy array time in milliseconds",(time.time()-start)*1000)
#numpy array
start=time.time()
result=a1+a2
print("python took:",(time.time()-start)*1000)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
a=np.array([5,6,9])
print(a)#convert list to numpy array
a=np.array([[1,2],[3,4],[5,6]])
print(a.ndim)#numpy array dimension
print(a.itemsize)#print bytes size of individual elements
print(a.dtype)#datatype of element

a=np.array([[1,2],[3,4],[5,6]],dtype=np.int32)
print(a.itemsize)#int32 memory size is 4 , float64 datatype memory size is 8

print(a.size)#total size of numpy array
print(a.shape)#rows and columns of numpy array
 
#placeholder
print(np.zeros((3,4)))#placeholder 0's
print(np.ones((3,4)))#placeholder 1's

print(np.arange(1,5))#print array of 4 numbers
print(np.arange(1,5,2))#print steps of 2(jumps 2 elements)

print(np.linspace(1,5,10))#split the range of number with linear spacing

print(a.shape)
print(a.reshape(2,3))#reshape to any shape but it have to have a same value while multiplying rows and columns value

print(a.ravel())#it will faltten it to one dimensional array, but it wont alter the original numpy array.


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#mathamatical function of numpy array

print(a.min())#print minimum value of all individual element
print(a.max())#print maximum value of all individual element
print(a.sum())#print sum of all elements in numpy array 

#axis

''' 
            axis
             |
             0

            1 2 3
  axis->1   4 5 6  
            7 8 9

'''
print(a.sum(axis=0))#sum the column values only
print(a.sum(axis=1))#sum the row values only

print(np.sqrt(a))#returns the suqare root of each individual element in numpy array, but wont affect the original array
print(np.std(a))#returns the standard deviation of the numpy array, but wont affect the original array

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])

print(a+b)#print addition operation
print(a-b)#print subtraction operation
print(a*b)#print multiplication operation
print(a/b)#print multiplication operation

print(a.dot(b))#print matrix dot multiplication operation

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Numpy: slicing/stacking and indexing with boolean arrays
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#topics
'''
    1)indexing and slicing
    2)iterating through arrays
    3)stacking together two arrays
    4)indexing with boolean arrays

'''

#indexing and slicing
a=np.array([6,7,8])
print(a[0:2])#slicing like python list
print(a[-1])#print in reverse order

a=np.array([[6,7,8],[1,2,3],[9,3,2]])
print(a[1,2])#1-row and 2 is column, returns the indexing element in array
print(a[0:2,2])
print(a[-1,0:2])#prints last row and 0th and 1st column values

print(a[:,:])# ':'iterate to all the element

for row in a:
    print(row)#print all the row with looping
for cell in a.flat:
    print(cell)#it flattening it as a single dimensional array and print every element in the numpy array
    #and access every individual array element

a=np.arange(6).reshape(3,2)#range of 6 elements and dimension is 3x2
b=np.arange(6,12).reshape(3,2)

print(np.vstack((a,b)))#print the vertical stack of row wise element in both a,b
print(np.hstack((a,b)))#print the horizantal stack of column wise element in both a,b in one dimensional array

a=np.arange(30).reshape(2,15)
print(a)
print(np.hsplit(a,3)) # horizantally split the array 'a' into three different array
print(np.vsplit(a,2))#vertically split the array 'a' into 2 different array
#how many partition should i make

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#boolean  expression - very power full

a=np.arange(12).reshape(3,4)
b=a>4
print(b)#return boolean expression either True or False in the matrix form by the condition of b=a>4

print(a[b])#Index of the array 'a' is array itself and it return every element that is True matching with the element in array 'a'

a[b]=-1
print(a)#return every matrix element and replace the elements with '-1' that satisfies the condition a>4


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Iterate numpy array using nditer

a=np.arange(12).reshape(3,4)
for row in a.flatten():
    print(row)
#nditer - more sophisticated way of iteration
#c-order - flows in the array elements from left to right -->right to left -->..
#f-order(fortran order) - flows in the array elements from top to down --> down to top -->..
 
for x in np.nditer(a,order='F'):
    print(x)#print element in the fortran order(F)

for x in np.nditer(a,op_flags=['readwrite']):
    x[...]=x*x#square and print all elements in array matrix using nditer
print(a)#square and print all elements in array matrix using nditer


b=np.arange(3,15,4).reshape(3,1)
print(b)

for x,y in np.nditer([a,b]):
    print(x,y)#access both the array element and take the second array element as common thing
    



  