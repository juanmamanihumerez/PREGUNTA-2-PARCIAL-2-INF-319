#!/usr/bin/env python
# coding: utf-8

# In[6]:


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2) + + fib(n-3)


# In[7]:


for x in range(7):
    print(fib(x))


# In[ ]:




