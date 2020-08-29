import numpy as np

in_layer = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
out_layer = np.array([[0,0,1,1]]).T

weight=2 * np.random.random((3, 1)) - 1

for i in range(10000):
    layer_0 = in_layer
    dot_prod = np.dot(layer_0,weight)
    layer_1 = 1/(1+np.exp(-dot_prod))
    l1_error = out_layer - layer_1
    check = layer_1*(1 - layer_1)
    l1_delta = l1_error * check
    weight += np.dot(layer_0.T , l1_delta)
print("output predicted is: \n",layer_1)