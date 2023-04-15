#!/usr/bin/env python
# coding: utf-8

# # Task 2- UNEMPLOYMENT ANALYSIS WITH PYTHON

# In[33]:


#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter("ignore")


# In[34]:


#importing the dataset from computer
df = pd.read_csv('C:/Users/preet/OneDrive/Desktop/Unemployment_Rate_upto_11_2020.csv')
df.head()


# In[35]:


#Checking for the null values in the dataset
df.isnull().sum()


# In[36]:


df.info()


# In[37]:


#checking for the corelation of all the features form the dataset
df.corr()


# In[38]:


corr =df.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr, cmap="Blues", annot=True)


# In[39]:


#Data Vitualizations
#taking a look at the estimated number of employees according to different regions of India
df.columns= ["States","Dates", "Frequency", "Estimated Unemployment Rate", "Estimated Employed", "Estimated Labour Participation Rate", "Region", "longitude", "latitude"]
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Region", data=df)
plt.show()


# In[40]:


#unemployment rate according to different regions of India
plt.figure(figsize=(12, 10))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=df)
plt.show()


# In[ ]:




