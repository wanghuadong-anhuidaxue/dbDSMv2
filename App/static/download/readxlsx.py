


import pandas as pd


import numpy as np








df = pd.read_excel('literature.xlsx',dtype=str)

np.save('literature',df.values)
data = np.load('literature.npy')


#print(len(data))
#print(data[:,4:]=='Specific tool')
#print(np.where(data[:,4:]=='Specific tool')[0])
#print(data[np.where(data[:,4:]=='Specific tool')[0]])


typeList = data[:,4:5]
print(len(np.unique(typeList)))




















