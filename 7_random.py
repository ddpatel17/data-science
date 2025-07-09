import numpy as np

x = np.random.seed(12)
print(x) # This will print the seed value

#rand()
print("rand(2,3)\n",np.random.rand(2,3))  # rand(row,column)

# randint(low, high, size)
print("randint :",np.random.randint(10,50,5)) # randint(min,max,number of element)

# shuffle
y = random.random(10)
print(y)
np.random.shuffle(y)
print("shuffle: ",y)

# randn()
print("randn",np.random.randn(2,3)) #randn(row,column)

# normal()
print("normal",np.random.normal(0,6,2))

# choice
print(np.random.choice(y))