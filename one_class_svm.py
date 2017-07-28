import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from sklearn import svm
import pandas as pd
from sklearn.cross_validation import train_test_split

class SVM:
    clf = svm.OneClassSVM(nu=0.05, kernel='rbf', gamma=1)

    def createTrainingData():
        x_path = 'csv/pedro_train.csv'
        dataset = pd.read_csv(x_path,header=-1)
        X = dataset.values
        return X

    def createTestingData():
        x_path = 'csv/dan_test.csv'
        dataset = pd.read_csv(x_path,header=-1)
        X = dataset.values
        return X


    def train(training_set):
        X_train = training_set
        n,g = SVM.chooseBestParams(X_train)
        file = open("train.txt", "a")
        file.write('N:'+str(n)+','+'G:'+str(g))
        file.close()
        SVM.clf = svm.OneClassSVM(nu=n, kernel='rbf', gamma=g)
        SVM.clf.fit(X_train)

    def test(testset):
        X_test = testset
        prediction = SVM.clf.predict(X_test)
        return prediction

    def splitTrainingData(X,percentage=0.6):
        limit = int(X.shape[0]*percentage)
        X_train = X[:limit]
        X_test = X[limit:]
        return (X_train,X_test)

    def chooseBestParams(X):
        prec_avg_arr = []
        best_avg = -1
        best_n_index = -1
        best_g_index = -1

        X_train,X_test = SVM.splitTrainingData(X)
        n = np.arange(0.01, 0.06, 0.001)
        g = np.arange(0.01, 1.1, 0.01)

        for i in range(len(n)):
            for j in range(len(g)):
                temp = svm.OneClassSVM(nu=n[i], kernel='rbf', gamma=g[j])
                temp.fit(X_train)

                y_pred_train = temp.predict(X_train)
                y_pred_test = temp.predict(X_test)

                n_error_train = y_pred_train[y_pred_train == 1].size
                n_error_test = y_pred_test[y_pred_test == 1].size

                train_precision = n_error_train / len(y_pred_train)
                test_precision = n_error_test / len(y_pred_test)

                avg = (train_precision + test_precision) / 2
                
                if avg>best_avg:
                    best_avg = avg
                    best_n_index = i
                    best_g_index = j
                

            best_nu = n[best_n_index]
            best_gamma = g[best_g_index]

            return (best_nu,best_gamma)

