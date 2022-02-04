#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Define a function which will take a number as argument and return its factorial.


# In[18]:


def factorial (x1):
    if x1 == 0:
        print("factorial of 0 is 1")
    else:
        fact = 1
       
        for i in range(1, x1+1):
            fact = fact*i
        print("The factorial of %d is %d"%(x1,fact))
x1=int(input("Enter the factorial number: "))
factorial(x1)


# In[ ]:





# In[ ]:




