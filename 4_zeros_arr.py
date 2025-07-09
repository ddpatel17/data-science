import numpy as np
        # np.zeros()
        # numpy.zeros(shape, dtype = None, order = 'C'
array = np.zeros(5)
print(array)
array1 = np.zeros(7,dtype=int)
print(array1)
array2 = np.zeros(3,float)
print(array2)
print(type(array2))# np.nd array
print(array2.dtype) # float64

a = np.zeros((3,2)) # 2d array
print(a)
# a1 = np.zeros(([4,3],dtype=int))
# print(a1)

d = np.zeros((4,3,5))
print(d)
print(type(d))# np.nd array
print(d.shape) #(4, 3, 5)
# d1 = np.zeros((5,2,3,dtype=int))
# print(d1)
