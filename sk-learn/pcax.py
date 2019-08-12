# https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA

import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# pca = PCA(n_components=1)
# print(pca.explained_variance_ratio_)  # 每个维度值差异百分比
# print(pca.singular_values_) # 每个维度的奇异值


pca = PCA(n_components=1).fit_transform(X)   # 降到一维

print(pca) #[[ 1.38340578][ 2.22189802][ 3.6053038 ][-1.38340578][-2.22189802][-3.6053038 ]]




