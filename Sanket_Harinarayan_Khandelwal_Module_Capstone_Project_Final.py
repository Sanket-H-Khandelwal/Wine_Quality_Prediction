#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi
import scipy.stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from collections import Counter
from IPython.core.display import display, HTML
sns.set_style('darkgrid')
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


# In[18]:


def df_read(url):
    """
    df is the dataframe where we will be saving the csv from the url
    """
    df=pd.read_csv(url, sep=";")
    return df


# In[32]:


# Remove spaces from column names
def rm(df_red):
    """
    df_red: we are passing the data frame 
    We will remove the spaces from the column names and return the dataset name on which we performed the function
    """
    df_red.columns = [x.strip().replace(' ','_') for x in df_red.columns]
    


# In[29]:


def covmax(x):
    """
    Passing the dataframe and creating a correlation matrix to get the relation between the variables
    """
    f, ax = plt.subplots(figsize=(10, 8))
    corr = x.corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
    square=True, ax=ax)
    ax.set_xticklabels(x.columns)
    ax.set_yticklabels(x.columns)
    plt.show()


# In[30]:


def countplots(df_red):
    """
    This will plot the quality on the x axis against the count
    """
    df_red["quality"] = pd.Categorical(df_red["quality"])
    sns.countplot(x="quality", data=df_red)
    plt.xlabel("Quality level of wine (0-10 scale)")
    plt.show()


# In[31]:


def factorplots(x):
    """
    Passing the dataframe and printing Alcohol percent in each level of red wine's quality
    
    """
    sns.factorplot(x="quality", y="alcohol", data=x, kind="strip")
    plt.xlabel("Quality l-evel of wine, 0-10 scale")
    plt.ylabel("Alcohol level in wine, % ABV")
    if x.equals(x):
        plt.title("Alcohol percent in each level of red wine's quality")
    plt.show()


# In[ ]:


def quality_citric(x):
    fig = plt.figure(figsize = (10,6))
    sns.barplot(x = 'quality', y = 'citric_acid', data = x)

