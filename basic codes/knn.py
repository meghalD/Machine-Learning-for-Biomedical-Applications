from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
import numpy as np
knn = KNeighborsClassifier(n_neighbors=6)

iris = datasets.load_iris() #training dataset

#make testing data
np.random.seed(0)
iris_X = iris['data']
iris_Y = iris['target']
indices = np.random.permutation(len(iris_X))
iris_X_test  = iris_X[indices[-10:]]

knn.fit(iris_X[indices[:-10]],iris_Y[indices[:-10]])
predicted = knn.predict(iris_X_test)
print("predicted by knn : ",predicted)
print("actual: ",iris_Y[indices[-10:]])
