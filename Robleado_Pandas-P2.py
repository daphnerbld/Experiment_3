#!/usr/bin/env python
# coding: utf-8


# In[2]:


# Importing numpy, pandas, and constants
import numpy as np
import pandas as pd
from math import *


# ## PROBLEM 2


# In[22]:


# Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars
print("First five rows with odd-numbered columns:")
cars.iloc[:5, ::2]


# In[23]:


#Display the row that contains the ‘Model’ of ‘Mazda RX4’
print("\nRow with the 'Mazda RX4':")
mazda_rx4 = cars[cars['Model'] == 'Mazda RX4']
mazda_rx4


# In[27]:


# How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
print("\nNumber of cylinders in 'Camaro Z28':")
camaro_z28_cyl = cars[cars['Model'] == 'Camaro Z28']['cyl'].values[0]
cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']]


# In[25]:


# Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
print("\nCylinders and gear type for 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic':")
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
selected_cars = cars[cars['Model'].isin(models)][['Model', 'cyl', 'gear']]
selected_cars

