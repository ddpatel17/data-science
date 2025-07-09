import numpy as np

        # cpoy() 
        # numpy.copy(array)

array1 = np.arange(0,10) # 10 not included 
print(array1)
array2 = np.copy(array1)
print(array2)

# list
l1 = [10,20,30,40,50] 
array3 = np.copy(l1)
print(array3)

# tuple
t1 = (60,70,80,90,100)
array4 = np.copy(t1)
print(array4)

