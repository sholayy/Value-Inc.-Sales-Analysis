#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[40]:


df = pd.read_csv("/Users/Sola/Desktop/Sola resume/Python+tableau/Sales Analysis/transaction2.csv",sep=';')


# In[41]:


df.head(50)


# In[42]:


df.info()


# In[43]:


df.isnull().sum()


# # working with calculations 

# In[45]:


df['CostPerTransaction'] = df['CostPerItem'] * df['NumberOfItemsPurchased']
df['SalesPerTransaction'] = df['SellingPricePerItem'] * df['NumberOfItemsPurchased']
df['ProfitPerTransanction'] = (df['SellingPricePerItem']- df['CostPerItem']) * df['NumberOfItemsPurchased']


# In[46]:


df.head()


# In[47]:


df['MarkUp']=  round((df['SalesPerTransaction'] - df['CostPerTransaction']) / df['CostPerTransaction'],2)
df.head()


# In[50]:


df['my_date'] = df['Day'].astype(str)+'-'+df['Month']+'-'+ df['Year'].astype(str)


# In[52]:


df['my_date'] = pd.to_datetime(df['my_date'])


# In[53]:


df.head()


# In[55]:


# using split to split the client keywords
split_col=df['ClientKeywords'].str.split(',',expand=True)
split_col


# In[56]:


df['ClientAge']= split_col[0]
df['Clienttype']= split_col[1]
df['ContractLength']= split_col[2]

df.head()


# In[58]:


# using replace function
df['ClientAge'] = df['ClientAge'].str.replace('[','')
df['ContractLength'] = df['ContractLength'].str.replace(']','')


# In[61]:


df['ItemDescription'] = df['ItemDescription'].str.lower()


# Merging with season file

# In[62]:


seasons= pd.read_csv("/Users/Sola/Desktop/Sola resume/Python+tableau/Sales Analysis/value_inc_seasons.csv",sep=';')


# In[63]:


# merging files
df1 = pd.merge(df,seasons, on ='Month')
df1.head()


# In[64]:


# dropping keywords 
to_drop = ['ClientKeywords', 'Day','Year','Month']
df1 = df1.drop(to_drop,axis=1)
df1.head()


# In[65]:


# export into a csv
df1.to_csv('ValueInc_cleaned.csv',index=False)


# In[66]:


pwd


# In[ ]:




