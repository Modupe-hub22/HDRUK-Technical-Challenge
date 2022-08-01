#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport


# In[16]:


#Read in the dataset
df = pd.read_csv(r'C:\Users\moa57\clean_mortality.csv')


# In[17]:


#Get information about df
df.info()


# In[18]:


#Get the column labels of the dataframe
df.columns


# In[22]:


#Run the profiler on some variables of interest

columns_of_interest = ['outcome', 'age', 'gendera', 'BMI',
       'hypertensive', 'diabetes',
       'deficiencyanemias', 'depression', 'Hyperlipemia', 'Renal.failure',
       'COPD', 'heart.rate', 'Systolic.blood.pressure',
       'Diastolic.blood.pressure', 'Respiratory.rate', 'temperature', 'SP.O2',
       'Urine.output', 'hematocrit', 'Leucocyte', 'Platelets', 'Neutrophils', 'Basophils', 'Lymphocyte',
       'PT', 'INR', 'NT.proBNP', 'Creatine.kinase', 'Creatinine',
       'Urea.nitrogen', 'glucose']
profile = ProfileReport(df.loc[:,columns_of_interest], 
                        title="Pandas Profiling Report")
profile


# In[ ]:





# In[ ]:




