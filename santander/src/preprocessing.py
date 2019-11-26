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

# 모든 열의 값 5개
# 각 열의 데이터 타입 등을 확인하여 타입 변경이 필요한 데이터를 파악
for col in otr.columns:
    print("{}\n".format(otr[col].head()))

# %%

# otr의 열의 개수, 열 별 데이터 타입, 사용 메모리 등을 확인 할 수 있다.
otr.info()
# float64(8), int64(23), object(17)
# memory usage: 4.9+ GB (실제 파일 크기와 다르다) 
# %%
# 24개의 고객 변수 중 수치형 변수
num_cols = [col for col in otr.columns[:24] if otr[col].dtype in ['int64', 'float64']]

otr[num_cols].describe()
# count - 개수
# meadn - 평균
# std - 데이터의 표준편차
# min - 최솟값
# 25% - 25% 값
# 50% - 50% 값
# 75% - 75% 값
# max - 최댓값
# %%
# 24개의 고객변수 중 범주형 변수
cat_cols = [col for col in otr.columns[:24] if otr[col].dtype in ['O']]   # 'O' -> object
otr[cat_cols].describe()

# %%
