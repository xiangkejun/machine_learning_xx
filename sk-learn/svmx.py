#二分类
from sklearn import svm
X = [[0, 0], [1, 1]] # [n_samples, n_features]
y = [0, 1]  #  class labels
clf = svm.SVC(gamma='scale')
clf.fit(X, y) 
print(clf.predict([[2., 2.]])) # 1

print(clf.predict([[-1., -1.]]))  # 0


