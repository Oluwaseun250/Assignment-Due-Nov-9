#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df= pd.read_csv("Basketball.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[10]:


df['Basketball'] = (df['LostGames'] / df['LostGames'].shift(1)


# In[ ]:




