import numpy as np 

# 1d
a = np.array([1, 2, 3])
b = np.array([1, 0, ]) # non value applicable 
print(a,b)

# 2d 
# a = ([[1,2,3][4,5,6]])
# b = ([[1,5,3][2,6]])

print("a==b :",a==b)
print("a!=b :",a!=b)

print("np.all(a==b) :",np.all(a==b))
print("np.any(a==b) :",np.any(a==b))

print("np.all(a!=b) :",np.all(a!=b))
print("np.any(a!=b) :",np.any(a!=b))    






                            # array_equal()
# Two arrays with the same shape and elements
a1 = np.array([1, 2, 3])
a2 = np.array([1, 2, 3])
print(a1,a2)

print(np.array_equal(a1,a2))

a3 = np.array([1,2,4])
print(a1,a3)
print(np.array_equal(a1,a3))

a4 = ([[1,3,4]])
print(np.array_equal(a3,a4))


