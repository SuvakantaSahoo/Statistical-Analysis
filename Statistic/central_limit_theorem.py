#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns


def clt(data,col,size):
    pop_mean = data[col].mean()
    
    sample_means = []
    for i in range(size):
        sample_means.append(data[col].sample(1000).mean())
    print('population mean for {} is {}:'.format(col,pop_mean))        
    print('mean of sample means for {} is {}:'.format(col,np.mean(sample_means)))
    sns.histplot(sample_means);

