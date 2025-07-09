import numpy as np 
        # linspace() 
        # numpy.linspace(start, stop, num = 50, endpoint = True, retstep = False, dtype = None, axis = 0)

a= np.linspace(1,10,5) # 1 and 10 included 
print(a)

a1= np.linspace(1,10,5,True) # 1 and 10 included and same output of a
print(a1)
a2= np.linspace(1,10,5,False) # 1 included but 10 not included and different output of a and a1
print(a2)

a3= np.linspace(1,10,5,True,dtype=int) # 1 and 10 included and same output of a
print(a3)
a4= np.linspace(1,10,5,False,dtype=int) # 1 and 10 included and same output of a
print(a4)