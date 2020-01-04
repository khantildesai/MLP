from MLP import Network
import numpy as np

net = Network([3,2,1])

net.feedforward(np.array([3,3,3]))

print(net.nodes)