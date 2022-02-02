#!/usr/bin/env python
# coding: utf-8

# In[5]:


word = input("Please Enter the Lottery number:").lower()
x1 = []

for i in word:
    x1.append(i)

print(x1)
result = max(x1,key = x1.count)
print("The maximum occuring character is:"+ result)
print("I select the character %c from the given sequence %s for the lottery."%(result,word)) 


# In[ ]:




