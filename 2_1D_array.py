import numpy as np 
# age = [10,20,30,40,50]
# age_np = np.array(age)
# print("array is =",age_np)

age = np.array([10,20,30,40,50,60,70])
print("age is =",age)
print(type(age)) # type of array 
print(age.dtype) # data type 
print(age.shape)

age2 = [10.5,20.5,10.5,100.50,10.500]
age2_np = np.array(age2)
print("float age =",age2_np)
print(age2_np.dtype)
print(age2_np.shape)