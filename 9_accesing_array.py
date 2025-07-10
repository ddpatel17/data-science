import numpy as np

array = np.array([[10,20,30],[40,50,60]])
print(array)

 #Access element at 1st row, 2nd column:
print(array[0,1]) # 20
print(array[1,2]) #60
print(array[1,]) # 40,50,60
print(array[0,]) # 10,20,30

 # Slicing Arrays like list in python
print("array = ",array)
print("1 =",array[0:1]) # 10,20,30 ?
print("2 =",array[1:2]) #40,50,60?
print("3 =",array[1:]) # 40,50,60
print("4 =",array[0:])# 10,20,30

b = array[:,1:2]
print("a[:,1:2]\n",b) # ([20][50])
print("a[:,1:2]\n",b.shape) # (2, 1)
print(array[:,1:]) # [[20 30] [50 60]]?
print(array[:2,1:]) #[[20 30] [50 60]]?


 #Boolean Indexing (can not use and and or operator)
c = array[array<60]
print("bool =",c)
print("bool shape =",c.shape)
print(array)
print(array[[0,1],[1,2]]) # [20 60]




# how to change value in array ?
array[1][1] =15
print(array) #[[10 20 30][40 15 60]]

array[0][0]= 20
print(array) #[[20 20 30] [40 15 60]]


x = [10,20,30,40,50,60]
x = np.array(x)
print(x)
x[2:4]=[100,200]
print(x) # [ 10  20 100 200  50  60]


x[x>=100]=5
print(x) # [10 20  5  5 50 60]