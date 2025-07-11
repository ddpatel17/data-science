import numpy as np 

a1 = np.array([1, 2, 3, -1, 5])
a2 = np.array([4, 0, 2, 7, 3])
print(a1,a2)

# 1. Logical AND (True where both conditions are True)
print("np.logical_and(a1,a2) :",np.logical_and(a1,a2)) # [ True False  True  True  True] ???
print("np.logical_and(a1<0,a2>3) :",np.logical_and(a1<0 , a1>3)) #[False, False, False, False, False]
print("np.logical_and(a1<0,a2>=5) :",np.logical_and(a1>0 , a1<=5)) #[True, True, True, False, True]
print("np.logical_and(a1<0,a2>5) :",np.logical_and(a1>0 , a2<5)) #[True, True, True, False, True]

# 2. Logical OR (True where at least one condition is True)
print("np.logical_or(a1,a2) :",np.logical_or(a1,a2)) #  [ True  True  True  True  True]???
print("np.logical_or(a1<0 , a1>=3) :",np.logical_or(a1<0 , a1>=3)) # [FALSE, FALSE, TRUE, TRUE, TRUE]
print("np.logical_or(a1>0 , a1<5) :",np.logical_or(a1>0 , a1<5)) # [TRUE, TRUE, TRUE, TRUE, TRUE]
print("np.logical_or(a1>0 , a2<5) :",np.logical_or(a1>0 , a2<5)) # [TRUE, TRUE, TRUE, FALSE, TRUE]

# 3. Logical NOT (True where the condition is False)
print("np.logical_not(a1 > 0) :",np.logical_not(a1 > 0)) # [False False False True False]
print("np.logical_not(a1,a2) :",np.logical_not(a1 , a2)) # [0 0 0 0 0]
print("np.logical_not(a1 & a2) :",np.logical_not(a1 & a2)) #[ True  True  True  True  True]
print("np.logical_not(a1<0 , a1>3) :",np.logical_not(a1<0 , a1>3)) # [TRUE, TRUE, TRUE, TRUE, TRUE]
print("np.logical_not(a1>0 , a1<5) :",np.logical_not(a1>0 , a1<5)) # [FALSE, FALSE, FALSE, TRUE, False]
print("np.logical_not(a1>0 , a2<5) :",np.logical_not(a1>0 , a2<5)) # [FALSE, FALSE, FALSE, TRUE, FALSE]

# 4. Logical XOR (True where only one of the conditions is True, not both)
#  When only one of the two conditions is True - result is True
#  When both are True or both are False - result is False

print("np.logical_xor(a1<0 , a1>3)) :",np.logical_xor(a1<0 , a1>3)) # [FALSE, FALSE, FALSE, TRUE, TRUE]
print("np.logical_xor(a1>0 , a1<5)) :",np.logical_xor(a1>0 , a1<5)) # [FALSE, FALSE, FALSE, TRUE, TRUE]
print("np.logical_xor(a1 > 0, a2 < 5) :",np.logical_xor(a1 > 0, a2 < 5)) # [False, False, False, False, False]