from sklearn.feature_selection import VarianceThreshold
#feature selection using variance threshold

X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
X=sel.fit_transform(X)
print(X)