import numpy as np

#Arithemetic Operations
ar7 = np.arange(9).reshape(3,3)
print(ar7)

ar7 = np.add(ar7, [10, 10, 10])
print(ar7)
ar7 = np.subtract(ar7, [1, 1, 1])
print(ar7)
ar7 = np.multiply(ar7, [1, 2, 3])
print(ar7)
ar7 = np.divide(ar7, [2, 3, 4])
print(ar7)

ar8 = np.array([[1,2,3],[4,5,6]])
ar9 = np.array([[10,20,30],[40,50,60]])
ar10 = np.add(ar8, ar9)
print(ar10)
print(np.divide(ar10, [11,11,11]))

#Comparision
ar11 = np.array([[1,2],[3,4]])
ar12 = np.array([[1,2],[3,4]])
print(ar11 == ar12)
print(np.array_equal(ar11, ar12))

#Aggregate Functions
ar21 = np.array([(1,2,3),(3,4,5)])
print(ar21.sum()) #sum(all elements)
print(ar21.sum(axis=1)) #sum(each row)
print(ar21.sum(axis=0)) #sum(each column)
print(ar21.min(), ar21.max())
print(ar21.mean())

#Copying
cp = ar21.copy()
print(cp)

#Sorting
print(np.sort(np.array([3,6,2,5,1])))

unordered = np.array([[7,6,5],[4,9,8]])
print(unordered)
print(np.sort(unordered, axis=1))
print(np.sort(unordered, axis=0))

#Subsetting
items = np.array([[3,4,2],[8,7,9],[4,3,5]])
print(items[2][0])

#Slicing
items = np.arange(4,25,2)
print(items)
print(items[::3])
print(items[2:7:3]) #start, end, steps
print(items[::-1])
print(items[items>10])

#Reshaping
ar1 = np.arange(12)
print(ar1)

ar2 = ar1.reshape(3,4)
print(ar2)

ar3 = np.array([['a','b'],['c','d'],['e','f']]).reshape(2,3)
print(ar3)

#Iterating
for itr in np.nditer(ar3, order='C'):
    print(itr, end=' ')
print()

for itr in np.nditer(ar3, order='F'):
    print(itr, end=' ')
print()

#Falttening
ar4 = ar3.flatten()
print(ar4)

ar5 = ar3.flatten(order='F')
print(ar5)

#Transposing
ar6 = np.transpose(ar2)
print(ar6)

#Joining or Concatinating
ar13 = np.array([[1,2],[3,4]])
ar14 = np.array([[5,6],[7,8]])

print(np.concatenate((ar13, ar14), axis=0))
print(np.concatenate((ar13, ar14), axis=1))

#Splitting
ar15 = np.arange(9)
print(np.split(ar15, 3))
print(np.split(ar15, [4,5]))
print(np.split(ar15, [2,4,6]))

ar16 = np.array([[1,2,3],[4,5,6]])
print(np.reshape(ar16, (3,2)))
print(np.resize(ar16, (3,4))) #Doesn't throw error

#Slicing
ar17 = np.ones((6,6), dtype=int)
ar17[1::2, 0::2] = 0
ar17[0::2, 1::2] = 0
print(ar17)

#Misc functions
ar20 = np.array([[1, 2, np.nan], [np.nan, 2, np.nan]])
print(np.isnan(ar20).sum())

print(np.char.add(['a','b'],['c','d']))
print(np.char.lower("AXION"))
print(np.char.capitalize("numpy"))
print(np.char.center("Data", 20, '*'))

