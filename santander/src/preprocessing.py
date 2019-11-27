# Please use VsCode
# vscode 에서 python파일 jupyter_notebook처럼 사용하기
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
# 수치형 데이터 unique
for col in num_cols:
    uniq = np.sort(otr[col].unique().astype(str))
    print('-' * 50)
    print('# col: {}, n_uniq: {}\nuniq:\n{}'.format(col, len(uniq), uniq))
# %%
# 24개의 고객변수 중 범주형 변수
cat_cols = [col for col in otr.columns[:24] if otr[col].dtype in ['O']]   # 'O' -> object
otr[cat_cols].describe()
# count -  총 개수
# unique - 값의 종류(고유값의 개수)
# top - 가장 빈도가 높은 값
# freq - top의 빈도수(데이터의 분포를 확인 할 수 있다. -> (freq/count) )
# %%
# 범주형 데이터의 고유값
for col in cat_cols:
    # uniq = np.unique(otr[col].astype(str))   # numpy를 이용하는 방법
    uniq = np.sort(otr[col].unique().astype(str))   # pandas를 이용하는 방법 -> 속도가 더 빠르다(느낌)
    print('-' * 50)
    print('# col: {}, n_uniq: {}\nuniq:\n{}'.format(col, len(uniq), uniq))

'''데이터를 분석하여 특징을 찾아보고 자신만의 방법으로 정리해 보기'''
# %%
# 데이터 시각화
import matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

skip_cols = ['ncodpers', 'renta']
for col in otr.columns:
    # 값이 너무 많아 시간이 걸리는 변수 skip
    if col in skip_cols:
        continue
    
    # 영역 구분
    print("-" * 50)
    print('col: ', col)

    # 그래프 크기(figsize)를 설정
    f, ax = plt.subplots(figsize=(20,15))

    # seaborn을 사용한 막대 그래프를 생성
    sns.countplot(x=col, data=otr, alpha=0.5)
    # show() 함수를 통해 시각화한다.
    plt.show()
# %%
