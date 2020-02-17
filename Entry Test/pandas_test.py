import pandas as pd
import matplotlib.pyplot as plt


data_frame = pd.read_csv('data/data_linear.csv')

x = data_frame.iloc[:,0]
y = data_frame.iloc[:,1]

plt.plot(x,y)

plt.title('Diagram')
plt.xlabel('Area')
plt.ylabel('Price')
plt.savefig('diagram.png')

plt.show()