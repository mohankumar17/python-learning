import pandas as pd
import numpy as np
#Series
ps1 = pd.Series([12,11,14,15,10,16])
'''print(ps1)
print(ps1[3:])
print(ps1[::-1])
print(ps1[::2])
print(ps1[2:4])
print('Max:', ps1.max())
print('Min:', ps1.min())
print('Mean:', ps1.mean())
print('Median:', ps1.median())

#Labels(names) can be assigned to indexes as well
ps2 = pd.Series([12,11,14], index=['a','b','c'])
print(ps2)
print(ps2['b']) #ps2[1] also works

#DataFrames
df1 = pd.DataFrame([[5,4,6],[3,1,2],[8,4,2],[7,9,2],[3,9,4]], index=['x1','x2','x3','x4','x5'], columns=['col1','col2','col3'])
print(df1)

print(len(df1)) #no.of.rows
print(df1.shape)
print(df1.index)
print(df1.columns)
print(df1.values)

#Slicing and Subsetting
print(df1[['col1','col2']])
print(df1.loc[['x1','x2']])
print(df1.iloc[0:2])

print(df1['col2']['x3'])
print(df1.loc['x3']['col2'])
print(df1.iloc[2]['col2'])'''

data = dict({'animal': ['cat','cat','snake','dog','dog','cat','snake','cat','dog','dog'],
          'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
          'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
          'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no' ]})
labels = ['a','b','c','d','e','f','g','h','i','j']

#sum, count, min, max, mean, median, std, var
#df2 = pd.DataFrame(data=data, index=labels)
#print(df2)
#print(df2.head()) #5 by default
#print(df2.head(3))
#print(df2.tail(2))
#print(df2.dtypes)
#print('Count Animals:', df2['animal'].count())
#print('Count Ages:', df2['age'].count()) #drop null values by default
#print('Sum of Ages:',df2['age'].sum())
#print('Concatenated priorities:',df2['priority'].sum())
#print('Max:',df2['age'].max())
#print('Min:',df2['age'].min())
#print('Mean:',df2['visits'].mean())

#print(df2['animal'].value_counts()) #frequecy of each value occurence
#print(df2.describe()) #give statistical information

#print(df2.drop_duplicates(['animal'])) #remove duplicates and keep first occurence of value

'''df3 = df2.groupby(by='animal')
for each in df3:
    print(each)'''

#print(pd.melt(df2)) #columns into rows
#print(df2.pivot(columns='animal')) #rows into columns

'''df4 = pd.DataFrame([[1,2,3],[4,5,6]], index=['x1','x2'], columns=['c1','c2','c3'])
df5 = pd.DataFrame([[7,8,9],[10,11,12]], index=['x3','x4'], columns=['c1','c2','c3'])
print(df4)
print(df5)

df6 = pd.concat([df4,df5], axis=0) #axis=0 by default
print(df6)

df7 = pd.concat([df4,df5], axis=1)
print(df7)'''

#print(df2.sort_values(by='age'))
#print(df2.sort_values(by='visits',ascending=False))

#print(df2.drop(columns=['age','priority']))

#print(df2.sample(n=3)) #select 3 random records

#print(df2.iloc[2:5])
#print(df2.iloc[:, [2,3]])
#print(df2.iloc[:][['animal','age']])

#print(df2.loc[:, 'animal':'visits'])
#print(df2.iloc[:, 1:4])

#print(df2.isna())
#print(df2['age'].isna().sum()) #count total nan values
#print(df2.dropna())
#print(df2['age'].fillna(df2['age'].mean()))

#df6 = pd.DataFrame([['A',1],['B',2],['C',3]], columns=['x1','x2'])
#df7 = pd.DataFrame([['A','T'],['B','F'],['D','T']], columns=['x1','x3'])
#print(df6)
#print(df7)

#print(pd.merge(df6, df7, how="inner", on='x1')) #Inner Join

#print(pd.merge(df6, df7, how="left", on='x1')) #Left Join

#print(pd.merge(df6, df7, how="right", on='x1')) #Right Join

#print(pd.merge(df6, df7, how="outer", on='x1')) #Outer Join

df8 = pd.DataFrame([['A',1],['B',2],['C',3]], columns=['x1','x2'])
df9 = pd.DataFrame([['B',2],['C',3],['D',4]], columns=['x1','x2'])
print(df8)
print(df9)


#print(pd.merge(df8, df9)) #Set Intersection
#print(pd.merge(df8, df9, how='outer')) #Set Union
print(pd.merge(df8, df9, how='outer', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])) #Set Difference (df8-df9)