# -*- coding: utf-8 -*-
"""Sales data analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KydhMUtkmIi8B_AbDxhqsWxwWDB04zTD
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import plotly.graph_objs as go
from plotly.offline import iplot

data = pd.read_csv("/content/Sales Data.csv")

data.head()

data.describe()

data.dtypes

data.isnull().sum()

data = data.dropna(how = "all")
data.shape

"""What is the best month for sale..?"""

'04/19/19 08:46'.split('/')[0]

def month(x):
    return str(x).split('/')[0]

"""Adding month column"""

data["Month"] = data['Order Date'].apply(month)

data.dtypes

data['Month'].unique()

filter = data['Month'] == 'Order Date'
len(data[~filter])

data = data[~filter]

data.shape

data.head()

data['Month']

data.dtypes

data['Price Each']

import numpy as np

data['Quantity Ordered'].isna().sum()
data['Quantity Ordered'].isin([np.inf, -np.inf]).sum()
data['Quantity Ordered'] = data['Quantity Ordered'].replace([np.inf, -np.inf, np.nan], 0)
data = data.dropna(subset=['Quantity Ordered'])
data['Quantity Ordered'] = data['Quantity Ordered'].astype('int')
data.dtypes

data['Sales'] = data['Quantity Ordered'] * data['Price Each']
data.head(5)

data.groupby('Month')['Sales'].sum()

'917 1st St, Dallas, TX 75001'.split(',')[1]

def city(x):
  return x.split(',')[1]

def city(x):
    if x and ',' in x:
        return x.split(',')[1]
    else:
        return np.nan
data['Purchase Address'] = data['Purchase Address'].astype(str)
data['city'] = data['Purchase Address'].apply(city)

data.groupby('city')['city'].count()

plt.bar(data.groupby('city')['city'].count().index, data.groupby('city')['city'].count())
plt.xticks(rotation = 'vertical')
plt.xlabel("City Names")
plt.ylabel("Received Orders")
plt.show()

"""What time should we display advertisements to maximise for product purchase..?"""

data['Hour'] = pd.to_datetime(data['Order Date']).dt.hour

keys = []
hours = []
for key, hour_df in data.groupby('Order Date'):
    keys.append(key)
    hours.append(len(hour_df))

data.groupby('Product')["Quantity Ordered"].sum().plot(kind="bar")

data.groupby('Product')["Price Each"].mean()

product = data.groupby('Product')["Quantity Ordered"].sum().index
quantity = data.groupby('Product')["Quantity Ordered"].sum()
prices = data.groupby('Product')["Price Each"].mean()

plt.figure(figsize=(40,24))
fig,ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.bar(product, quantity, color='g')
ax2.plot(product, prices, 'b-')
ax1.set_xticklabels(product, rotation='vertical', size=8)

data.shape

df = data[data["Order ID"].duplicated(keep=False)]
df.head(20)

#df['Grouped'] = df.groupby("Order ID")['Product'].transform(lambda x: ','.join(x))

df.shape

df2 = df.drop_duplicates(subset=["Order ID"])

df2["Grouped"].value_counts()[0:5].plot.pie()

values = df2['Grouped'].value_counts()[:5]
labels = df2['Grouped'].value_counts()[:5].index

# Import the necessary function from the go module
from plotly.graph_objs import Pie

# Create the pie chart
traco = Pie(labels=labels, values=values,
            hoverinfo='label+percent', textinfo='value',
            textfont=dict(size=25),
            pull=[0, 0, 0, 0.2, 0])

# Execute cell 'ipython-input-40-1e1dc9cf9574'
df2 = df.drop_duplicates(subset=["Order ID"])

# Execute cell 'ipython-input-41-1e1dc9cf9574'
df2["Grouped"].value_counts()[0:5].plot.pie()

# Execute cell 'ipython-input-43-1e1dc9cf9574'
values = df2['Grouped'].value_counts()[:5]
labels = df2['Grouped'].value_counts()[:5].index

# Execute cell 'ipython-input-49-1e1dc9cf9574'
# Import the necessary function from the go module
from plotly.graph_objs import Pie

# Create the pie chart
trace = Pie(labels=labels, values=values,
            hoverinfo='label+percent', textinfo='value',
            textfont=dict(size=25),
            pull=[0, 0, 0, 0.2, 0])

# Execute cell 'ipython-input-53-1e1dc9cf9574'
iplot([trace])