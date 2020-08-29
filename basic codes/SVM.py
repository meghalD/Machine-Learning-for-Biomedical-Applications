from sklearn import svm
import matplotlib.pyplot as plt


x = [1,5,1.5,8,1,9, 2,3,7,8,1.8,6.5]
y = [2,8,1.8,8,0.6,11,4,6,8,6,3,10]
X=[]
Y=[0,1,0,1,0,1,0,0,1,1,0,1]

for i in range(len(x)):
    t=[]
    t.append(x[i])
    t.append(y[i])
    X.append(t)
#print(X)

plt.scatter(x,y)

clf = svm.SVC(kernel='linear')
clf.fit(X, Y)
x1=input("enter x value to predict its class :")
y1=input("enter y value to predict its class :")
print(clf.predict([[x1,y1]]))
plt.show()