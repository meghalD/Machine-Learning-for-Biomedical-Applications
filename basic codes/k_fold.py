from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import KFold, cross_val_score
import numpy as np

x = [1,5,1.5,8,1,9, 2,3,7,8,1.8,6.5]
y = [2,8,1.8,8,0.6,11,4,6,8,6,3,10]
X=[]
Y=[0,1,0,1,0,1,0,0,1,1,0,1]

for i in range(len(Y)):
    if Y[i]==0:
        Y[i]="benign tumor "
    else:
        Y[i]="malignant tumor"

for i in range(len(x)):
    t=[]
    t.append(x[i])
    t.append(y[i])
    X.append(t)
model= RandomForestClassifier(n_estimators=1000)
kfold = KFold(12,n_folds=10)
print(cross_val_score(model, X, Y, cv=kfold, n_jobs=1))