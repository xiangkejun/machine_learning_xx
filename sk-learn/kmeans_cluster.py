## https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])


# kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
pred = KMeans(n_clusters=2, random_state=0).fit_predict(X)

print(pred)  # [1 1 1 0 0 0]
plt.scatter(X[:,0],X[:,1],c=pred)
plt.show()

# print(kmeans.labels_) # [1 1 1 0 0 0]

# print(kmeans.predict([[0, 0], [12, 3]])) # [1 0]

# print(kmeans.cluster_centers_) # [[10.  2.] [ 1.  2.]]