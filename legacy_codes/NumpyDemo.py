#Numpy is used to manage multi-dimensional arrays
#It is used for scientific and numerical computing
#It is Fast, conventional(lot of functions) and consumes less memory

import numpy as np

items = np.array([(1,2,3),(4,5,6),(1,4,6),(7,3,6)], dtype=int)
print(items)

zeros = np.zeros((3,4), dtype=int)
print(zeros)

ones = np.ones((3,4), dtype=float)
print(ones)

ar22 = np.arange(5,12,2)
print(ar22)

ar23 = np.linspace(0,2,9)
print(ar23)

ar24 = np.full((2,2), 7)
print(ar24)

idMat = np.eye(4)
print(idMat)

ar25 = np.random.rand(3,4)
print(ar25)

ar26 = np.random.randint(4, size=(5,3))
print(ar26)

ar27 = np.empty((3,2))
print(ar27)

print(items.shape) #dimensions (rows,columns)
print(len(items)) #No.of.rows
print(items.ndim) #dimensions (1D or 2D or any)
print(items.size) #tot elements
print(items.dtype) #datatype of elements
print(items.astype(float))

for itr in np.nditer(ar22):
    print(itr, end=' ')
print()



