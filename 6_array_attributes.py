import numpy as np

# 3D array
a = np.array([[[311, 312, 313],
               [321, 322, 323],
               [331, 332, 333]],
              [[211, 212, 213],
               [221, 222, 223],
               [231, 232, 233]],
              [[111, 112, 113],
               [121, 122, 123],
               [131, 132,133]]])
print(a)

# 2D array
b =np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)

# 1D array
c =np.array([5,6,10,12])
print(c)

        # array attributes 
# ndarray.size
print("size of a:"a.size)
print("size of b:"b.size)
print("size of c:"c.size)

# ndarray.shape
print("shape of a:"a.shape)
print("shape of b:"b.shape)
print("shape of c:"c.shape)

# ndarray.T
print("Transpose\n a:"a.T)
print("Transpose\n b:"b.T)
print("Transpose c:"c.T)

# ndarray.dtype
print("Datatype a:"a.dtype)
print("Datatype b:"b.dtype)
print("Datatype c:"c.dtype)

# ndarray.ndim
print("ndim",a.ndim)
print("ndim",b.ndim)
print("ndim",c.ndim)

# ndarray.itemsize
print("itemsize a",a.itemsize)
print("itemsize b",b.itemsize)
print("itemsize c",c.itemsize)

# ndarray.nbytes
print("nbytes a",a.nbytes)
print("nbytes b",b.nbytes)
print("nbytes c",c.nbytes)