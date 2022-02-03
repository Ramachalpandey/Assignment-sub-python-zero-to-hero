#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python code to find key with Maximum value in Dictionary

# Dictionary Initialization
Mobile_data = {'motorola':5000, 'nokia':4500, 'oppo' : 6500, 'iphone': 100000, 'mi': 2500}

#list of mobile  values in m
m = list(Mobile_data.values())
 
# list of mobile keys in p
p = list(Mobile_data.keys())
 
print("The maximum mobile price is  " + p[m.index(max(m))])


# In[ ]:




