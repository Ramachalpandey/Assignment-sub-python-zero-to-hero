#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Assignment5: Use filter function to filter out the elements from a list that are divisible by 3 & 5.

list_1 = list(range(1,20))
  
Result_1 = list(filter(lambda x: (x % 3 == 0), list_1)) 
Result_2 = list(filter(lambda x: (x % 5 == 0), list_1)) 
  
print(Result_1,"This number only divisible by 3") 
print(Result_2,"This number only divisible by 5") 


# In[ ]:




