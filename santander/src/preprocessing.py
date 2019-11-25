# Please use VsCode

#%% 
import pandas as pd
import numpy as np
import os

os.chdir(os.getcwd() + '/santander')

#%%
otr = pd.read_csv(os.getcwd() + '/data/train_ver2.csv')
#%%
otr.shape   # (13647309, 48)
#%%
otr.head()

# %%
for col in otr.columns:
    print("{}\n".format(otr[col].head()))

# %%
otr.info()

# %%
