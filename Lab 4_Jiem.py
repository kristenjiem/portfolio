#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 2. Import Python Libraries
import pandas as pd
import numpy as np


# In[2]:


# Expand the number of columns
pd.set_option('display.max_columns', 500)


# In[3]:


dir(pd)


# In[4]:


# define variables for the csv files, this step is not mandatory 
#but it will help to understand the importing data step in Python

File_1 = "Salaries.csv"


# In[5]:


# Read the csv file 
raw_df = pd.read_csv(File_1)


# In[6]:


#Check if the dataset is loaded
raw_df.head()


# In[7]:


# CREATING A NEW COLUMN WITH A DEFAULT ENTRY FOR EVERYTHING (BENCHMARKS is 70000)
raw_df["Benchmarks"] = 70000


# In[8]:


raw_df.head()


# In[9]:


# CREATING A NEW COLUMN WITH A DEFAULT ENTRY FOR EVERYTHING (AGE is 50)
raw_df["Age"] = 50


# In[10]:


raw_df.head()


# In[11]:


# MAKE A NEW COLUM WITH A CALCULATION
raw_df["Salary_score"] = round(raw_df["salary"] / raw_df["Benchmarks"],2)
raw_df.head()


# In[12]:


raw_df.columns


# In[13]:


# DROPPING a COLUMN
# Method 1: Subset the dataframe by including only spescific columns.
Subset_raw_df=raw_df[['rank','discipline','service']]
Subset_raw_df.head()


# In[15]:


Subset2_raw_df=raw_df[['phd', 'sex', 'salary', 'Benchmarks', 'Age', 'Salary_score']]
Subset2_raw_df.head()


# In[16]:


# Method 2: Use the drop method to drop the salary column
#(to drop the row, use axis=1)
#(to drop the column, use axis=0)
Subset3_raw_df=raw_df.drop(['sex','salary'], axis=1)
Subset3_raw_df.head()


# In[18]:


# select some columns from the original dataframe
subset_raw_df=raw_df[['rank','discipline','service']]

# check the created dataframe
subset_raw_df.head()


# In[19]:


# Change column names
subset_raw_df.columns = ["Original_Rank", "discipline_new",'service_new']

# check the change
subset_raw_df.head()


# In[20]:


# We can also use the rename method
#{original name:new name}

#inplace 
#(true) means that you are communicating with Python to override the original dataset
#(false) will make a new subset

subset_raw_df.rename(columns={'Original_Rank':'new_Rank','discipline_new':'new_discipline'},inplace=True)
subset_raw_df.head()


# In[21]:


df = pd.read_csv(File_1)


# In[22]:


# Reorder the columns
column_names=['service', 'rank', 'discipline']
df_new = df.reindex(columns=column_names)
df_new.head()


# In[23]:


# Method 2 to reorder the columns
df_new = df.reindex(columns=['service', 'rank', 'discipline'])
df_new.head()


# In[ ]:




