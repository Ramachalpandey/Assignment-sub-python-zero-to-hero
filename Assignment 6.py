#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Assignment 6: Floor divison of any two number by using Decorators.

def decorators(fun):
    def deno(x1, x2):
        if x1 < x2 :
            x1, x2 = x2, x1
        return fun(x1, x2)
    return deno

@decorators
def div(x1, x2):
    return  x1 // x2

x1 =int(input("Enter First value: "))
x2 =int(input("Enter Second value: "))
print(x1,x2)


print(div(x1, x2))


# In[ ]:




