from sklearn.ensemble import RandomForestClassifier

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
model.fit(X, Y)
#Predict Output
x1=input("enter x value to predict its class :")
y1=input("enter y value to predict its class :")

predicted= model.predict([[x1,y1]])
print(predicted)