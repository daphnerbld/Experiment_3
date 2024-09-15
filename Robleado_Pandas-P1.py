#!/usr/bin/env python
# coding: utf-8


# In[2]:


# Importing numpy, pandas, and constants
import numpy as np
import pandas as pd
from math import *


# ## PROBLEM 1

# In[17]:


#Load the corresponding .csv file into a data frame named 'cars'
cars = pd.read_csv('cars.csv')
cars


# In[21]:


#Display the first five rows of the data frame
print("First five rows of the 'cars' data frame:")
cars.head()


# In[20]:


#Display the last five rows of the data frame
print("\nLast five rows of the 'cars' data frame:")
cars.tail()
