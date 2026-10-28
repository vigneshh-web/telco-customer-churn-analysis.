#!/usr/bin/env python
# coding: utf-8

# # Employee Data Analysis

# In[2]:


numbers = list(range(1000))


# In[ ]:


get_ipython().run_line_magic('timeit', '[n * 2 for n in numbers]')


# In[5]:


get_ipython().run_cell_magic('timeit', '', 'result = []\nfor n in numbers:\n    result.append(n * 2)\n')

