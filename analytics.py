import pandas as pd
import numpy as np

data = pd.read_csv('AnalyticsGC.csv')
# print(data['y'])

l = data.shape[0]
# print(l)
y = data['y']

y_pred = [0]
for i in range(l-1):
	val = data['x4'][i] - data['x1'][i]
	if(val>0):
		y_val = 1
	else:
		y_val = 0
	y_pred.append(y_val)

y_pred = np.array(y_pred)
nmr = 0
dnm = 0
for i in range(l):
	dnm += 1
	if(y_pred[i] == y[i]):
		nmr += 1

acc = nmr/dnm
print (acc)