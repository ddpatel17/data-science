import numpy as np 

# 1d
a = np.array([1, 2, 3])
b = np.array([1, 0,None]) # non value applicable 
print(a,b)



print("a==b :",a==b) # [ True False False]
print("a!=b :",a!=b) # [False  True  True]

print("np.all(a==b) :",np.all(a==b)) # False
print("np.any(a==b) :",np.any(a==b)) # True

print("np.all(a!=b) :",np.all(a!=b)) # False
print("np.any(a!=b) :",np.any(a!=b)) # True 

#2d 
a1 = np.array([[1,2,3],[4,5,6]])
b1 = np.array([[1,5,3],[2,6,None]])
print(type(a1))
print(a1.dtype)
print(a1.shape)


print("a1==b1 :",a1==b1) # [[ True False  True] [False False False]]
print("a1!=b1 :",a1!=b1) #  [[False  True False] [ True  True  True]]

print("np.all(a1==b1) :",np.all(a1==b1)) # False
print("np.any(a1==b1) :",np.any(a1==b1)) # True 

print("np.all(a1!=b1) :",np.all(a1!=b1)) # False
print("np.any(a1!=b1) :",np.any(a1!=b1)) # True 
   







                            # array_equal()
# Two arrays with the same shape and elements
a1 = np.array([1, 2, 3])
a2 = np.array([1, 2, 3])
print(a1,a2)

print(np.array_equal(a1,a2)) # True

a3 = np.array([1,2,4])
print(a1,a3)
print(np.array_equal(a1,a3)) # False

a4 = ([[1,3,4]])
print(np.array_equal(a3,a4)) # False


