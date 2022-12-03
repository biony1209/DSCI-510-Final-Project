#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd


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


df['covid_status'] = 1
cf['covid_status'] = 0


# In[52]:


df


# In[53]:


cf

