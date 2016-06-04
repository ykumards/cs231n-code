## NN classifier
import numpy as np

class NearestNeighbor(object):
    def __init__(self):
        pass

    def train(self, X, Y):
        """
        X is N x D dimensional array which is out input
        Y is the array of N labels
        """
        self.Xtr = X
        self.ytr = Y
        # NN model just needs to store all the training data in memory
        # It uses this to compare with a new test data-point

    def predict(self, X):
        num_test = X.shape[0] #Get the number of entires
        Ypred = np.zeroes(numtest, dtype=self.ytr.dtype) # The type for test is same as that of train

        for i in xrange(numtest):
            # Use L1 distance
            distances = np.sum(np.abs(self.Xtr - X[i,:]), axis=1)
            # For L2 distance
            #distances = np.sqrt(np.sum(np.square(self.Xtr - X[i,:]), axis = 1))

            min_index = np.argmin(distances) #get the index of the least value
            # Match that with the index of y
            Ypred[i] = self.ytr[min_index]

        return Ypred


        
