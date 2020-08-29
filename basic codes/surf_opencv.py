import cv2
from matplotlib import pyplot as plt

filename = input("enter image(jpg/png) path with the extension : ")
img = cv2.imread(filename,0)    #read file
surf = cv2.ORB_create() #create ORB Descriptors
kp, des = surf.detectAndCompute(img,None)
img2 = cv2.drawKeypoints(img,kp,None,color=(0,255,0),flags=0) #draw keypoint found on the image
plt.imshow(img2),plt.show()