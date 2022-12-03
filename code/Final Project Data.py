#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import seaborn as sns
import maths


# In[43]:


df = pd.read_csv('covidtest.csv')
bf = pd.read_csv('data01.csv')


# In[44]:


df.rename({'date_died': 'outcome'}, axis=1, inplace=True)


# In[45]:


cf = bf[["ID", "outcome", "age", "gendera", "hypertensive", "diabetes"]]


# In[46]:


cf.rename({'ID': 'id', 'gendera': 'sex', 'hypertensive': 'hypertension'}, axis=1, inplace=True)


# In[47]:


transform={2:1,1:0}
df = df.replace({'sex':transform,'hypertension':transform, 'diabetes':transform})


# In[48]:


cf = cf.replace({'sex':transform})


# In[49]:


df['outcome'][df['outcome']!='9999-99-99']=1.0


# In[50]:


df['outcome'][df['outcome']!=1]=0.0


# In[51]:


df['covid_status'] = 0
cf['covid_status'] = 1


# In[52]:


frames = [df, cf]

result = pd.concat(frames, ignore_index=True)


# In[53]:


result = result[~result['outcome'].isnull()]
result['outcome'] = result['outcome'].astype(int)
result['age'] = result['age'].astype(int)
result['sex'] = result['sex'].astype(int)
result['hypertension'] = result['hypertension'].astype(int)
result['diabetes'] = result['diabetes'].astype(int)
result['covid_status'] = result['covid_status'].astype(int)


# In[54]:


result = result[result['outcome'] != 98]
result = result[result['sex'] != 98]
result = result[result['hypertension'] != 98]
result = result[result['diabetes'] != 98]


# In[55]:


df


# In[56]:


cf

