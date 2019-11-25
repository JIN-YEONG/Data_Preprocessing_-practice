# 고객이 구매할 것으로 예상되는 제품 상위 7개
# 최대 7개의 제품을 예측
# 평가 척도 MAP@7


import numpy as np

def apk(actual, predicted, k=7, defalut=0.0):
    # actual = [1,1,1,1,1,1,1]
    # predicted = [0,0,0,0,0,0,0]
    
    if len(predicted) > k:
        predicted = predicted[:k]

    score=0.0,
    num_hits=0.0

    for i, p in enumerate(predicted):
        # 점수를 부여하는 조건
        # 1. 예측값이 정답 (p in actual)
        # 2. 예측값이 중복이 아님 (p not in predicted[:i])

        if p in actual and p not in predicted[:i]:
            num_hits += 1.0
            score += num_hits / (i + 1.0)

    if not actual:
        return defalut

    return score / min(len(actual), k)

def mapk(actual, predicted , k=7, default = 0.0):
    # actual = [[1,1,1,1,1,1,1]]
    # predicted = [[0,0,0,0,0,0,0]]

    return np.mean([apk(a,p,k,default) for a,p in zip(actual, predicted)])

