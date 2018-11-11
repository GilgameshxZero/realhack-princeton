
# coding: utf-8

# In[304]:


import pandas as pd
import numpy as np


# In[305]:


df = pd.read_csv("/Users/meistn1/Desktop/categ_data.csv")


# In[306]:


df.shape


# In[307]:


check = np.asarray(df.iloc[:,6])
print(check)


# In[308]:


check = np.asarray(df.iloc[:,6])
idx_del = []
for i, check_row in enumerate(check):
    if check_row==0.0:
        idx_del.append(i)


# In[309]:


df_new = df.drop(idx_del, inplace=False)


# In[310]:


df_new.shape


# In[311]:


df_new.drop(['Unnamed: 0', 'Check'], axis=1)


# In[312]:


df_new = df_new.reset_index()


# In[313]:


df_new.head()


# In[314]:


for idx, row in df_new.iterrows():
    if (df_new.iloc[idx,2] == "January"):
        df_new.iloc[idx,2]="01"
    if (df_new.iloc[idx,2] == "February"):
        df_new.iloc[idx,2]="02"
    if (df_new.iloc[idx,2] == "March"):
        df_new.iloc[idx,2]="03"
    if (df_new.iloc[idx,2] == "April"):
        df_new.iloc[idx,2]="04"
    if (df_new.iloc[idx,2] == "May"):
        df_new.iloc[idx,2]="05"
    if (df_new.iloc[idx,2] == "June"):
        df_new.iloc[idx,2]="06"
    if (df_new.iloc[idx,2] == "July"):
        df_new.iloc[idx,2]="07"
    if (df_new.iloc[idx,2] == "August"):
        df_new.iloc[idx,2]="08"
    if (df_new.iloc[idx,2] == "September"):
        df_new.iloc[idx,2]="09"
    if (df_new.iloc[idx,2] == "October"):
        df_new.iloc[idx,2]="10"
    if (df_new.iloc[idx,2] == "November"):
        df_new.iloc[idx,2]="11"
    if (df_new.iloc[idx,2] == "December"):
        df_new.iloc[idx,2]="12"
    
df_new.head()


# In[315]:


df_new = df_new.drop(['index', 'Unnamed: 0', 'Check'], axis=1)


# In[316]:


df_new.head()


# In[317]:


df_new['date'] = 'date'


# In[318]:


df_new.head()


# In[319]:


df_new.iloc[0,0]


# In[320]:


for idx, row in df_new.iterrows():
    df_new.iloc[idx,5] = str(df_new.iloc[idx,0]) + "/" + str(df_new.iloc[idx,1]) + "/" + str(df_new.iloc[idx,2])


# In[321]:


df_new.head()


# In[322]:


df_new = df_new.drop(['Time', 'Unnamed: 2', 'Unnamed: 3'], axis=1)


# In[323]:


df_new.head()


# In[324]:


df_new.Q_Categ.unique()[1:13]


# In[325]:


unique_date = df_new.date.unique()
q_zeros = (len(unique_date), len(df_new.Q_Categ.unique()[1:13]))
uniq_finalQ = df_new.Q_Categ.unique()[1:13]
df_finalQ = pd.DataFrame(data=np.zeros(q_zeros), index=unique_date, columns=uniq_finalQ)

uniq_finalA = np.append(df_new.A_Categ.unique()[0:2], df_new.A_Categ.unique()[3:13])
a_zeros = (len(unique_date), len(uniq_finalA))
df_finalA = pd.DataFrame(data=np.zeros(a_zeros), index=unique_date, columns=uniq_finalA)


# In[326]:


df_finalQ.head()


# ### df_finalQ

# In[327]:


for idx, row in df_new.iterrows():
    for finalQ_idx in df_finalQ.index:
        if df_new.iloc[idx,2] == finalQ_idx: 
            categ = df_new['Q_Categ'][idx] #idx
            if categ in uniq_finalQ:
                df_finalQ.loc[finalQ_idx, categ] = df_finalQ.loc[finalQ_idx, categ] + 1


# In[328]:


df_finalQ.head()


# In[332]:


df_finalQ.to_csv('df_finalQ.csv')


# ### df_finalA

# In[330]:


for idx, row in df_new.iterrows():
    for finalA_idx in df_finalA.index:
        if df_new.iloc[idx,2] == finalA_idx:
            categ = df_new['A_Categ'][idx] #idx
            if categ in uniq_finalA:
                df_finalA.loc[finalA_idx, categ] = df_finalA.loc[finalA_idx, categ] + 1


# In[331]:


df_finalA.head()


# In[338]:


df_finalA.to_csv('df_finalA.csv')
