#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


df = pd.read_csv('covidtest.csv')
bf = pd.read_csv('noncovid.csv')


# In[7]:


df.rename({'date_died': 'outcome'}, axis=1, inplace=True)


# In[8]:


cf = bf[["ID", "outcome", "age", "gendera", "hypertensive", "diabetes"]]


# In[9]:


cf.rename({'ID': 'id', 'gendera': 'sex', 'hypertensive': 'hypertension'}, axis=1, inplace=True)


# In[10]:


transform={2:1,1:0}
df = df.replace({'sex':transform,'hypertension':transform, 'diabetes':transform})


# In[11]:


cf = cf.replace({'sex':transform})


# In[12]:


df['outcome'][df['outcome']!='9999-99-99']=1.0


# In[13]:


df['outcome'][df['outcome']!=1]=0.0


# In[14]:


df['covid_status'] = 0
cf['covid_status'] = 1


# In[15]:


df['outcome'] = df['outcome'].dropna().astype('uint8')


# In[16]:


df


# In[17]:


cf = cf.dropna()


# In[18]:


cf['outcome'] = cf['outcome'].astype(int)


# In[19]:


cf

