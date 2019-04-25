import numpy as np
from matplotlib import pyplot
from numpy import tanh


class NeuralNetwork(object):

    def __init__(self, weights_txt):
        self.weights = self.load_weights(weights_txt)

    def load_weights(self, weights_txt):

        return weights_txt

    def train(self, iterations):




    def predict(self):
        pass

    def back_prop(self):

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

