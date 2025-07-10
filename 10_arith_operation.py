import numpy as np

a = np.array([10,20,30])
b = np.array([1,2,3])
print(a,b)

 #basic maths operations 
# Both arrays must be of same shape, or be broadcast-compatible.
print("a+b =",a+b)
print("a-b =",a-b)
print("a*b =",a*b)
print("a/b =",a/b)


 #Scalar Operations.
print("scalar operation of a = ",a)
print("a+2 =",a+2)
print("a-2 =",a-2)
print("a*2 =",a*2)
print("a/2 =",a/2)
print("scalar operation of b = ",b)
print("b+2 =",b+2)
print("b-2 =",b-2)
print("b*2 =",b*2)
print("b/2 =",b/2)

#Mathematical Functions
print("math operation of a =",a)
print("sin(a) =",np.sin(a))
print("cos(a) =",np.cos(a))
print("exp(a) =",np.exp(a))
print("sqrt(a) =",np.sqrt(a))
print("log(a) =",np.log(a))
print("math operation of b =",b)
print("sin(b) =",np.sin(b))
print("cos(b) =",np.cos(b))
print("exp(b) =",np.exp(b))
print("sqrt(b) =",np.sqrt(b))
print("log(b) =",np.log(b))


 #Comparison Operations
print("comparison operator of a =",a)
print(a>15)
print(a<15)
print("comparison operator of b =",b)
print(b>2)
print(b<2)

 # Matrix Operations (Not Element-wise)
A = ([[1,2], [3,4]])
B = ([[5,6],[7,8]])
print("A \n",A)
print("B \n",B)
# print("A@B \n",A @ B)
# print("A@B\n",A @ B)
# print("B@A\n",(B @ A))
print("dot(B,A)\n",np.dot(B,A)) 


 # Aggregate Functions
print("aggregate function a =",a)
print("sum(a) =",np.sum(a))
print("mean(a) =",np.mean(a))
print("min(a) =",np.min(a))
print("max(a) =",np.max(a))
print("aggregate function b =",b)
print("sum(b) =",np.sum(b))
print("mean(b) =",np.mean(b))
print("min(b) =",np.min(b))
print("max(b) =",np.max(b))
