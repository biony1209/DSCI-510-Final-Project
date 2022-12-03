#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[8]:


covid = pd.read_csv('covidtest.csv')
noncovid = pd.read_csv('data01.csv')


# In[44]:


covid.rename({'date_died': 'outcome'}, axis=1, inplace=True)


# In[45]:


noncovid = bf[["ID", "outcome", "age", "gendera", "hypertensive", "diabetes"]]


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


df['covid_status'] = 1
cf['covid_status'] = 0


# In[55]:


df


# In[56]:


cf

