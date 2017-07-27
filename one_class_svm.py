import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from sklearn import svm
import pandas as pd

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

clf = svm.OneClassSVM(nu=0.05, kernel='rbf', gamma=23.308900000000001)

def train():
    X_train = createTrainingData()
    clf.fit(X_train)

def test():
    X_test = createTestingData()
    return clf.predict(X_test)


'''
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)

n_error_train = y_pred_train[y_pred_train == 1].size
n_error_test = y_pred_test[y_pred_test == -1].size

train_precision = n_error_train/len(y_pred_train)
test_precision = n_error_test/len(y_pred_test)

#(0.0027000000000000001, 0.0001, 23.308900000000001)

print('TRAIN:',train_precision*100,'%')
print('TEST:',test_precision*100,'%')


def selectBestParam(X_train, X_test):
    gammas = np.arange(0.0001, 100, 0.0001)

    prec_train_arr = []
    prec_test_arr = []
    prec_avg_arr = []

    for g in gammas:
        clf = svm.OneClassSVM(nu=0.05, kernel='rbf', gamma=g)
        clf.fit(X_train)

        y_pred_train = clf.predict(X_train)
        y_pred_test = clf.predict(X_test)

        n_error_train = y_pred_train[y_pred_train == 1].size
        n_error_test = y_pred_test[y_pred_test == -1].size

        train_precision = n_error_train / len(y_pred_train)
        test_precision = n_error_test / len(y_pred_test)

        prec_train_arr.append(train_precision)
        prec_test_arr.append(test_precision)
        prec_avg_arr.append((train_precision + test_precision) / 2)

    best_train_index = prec_train_arr.index(max(prec_train_arr))
    best_test_index = prec_test_arr.index(max(prec_test_arr))
    best_avg_index = prec_avg_arr.index(max(prec_avg_arr))

    best_train_gamma = gammas[best_train_index]
    best_test_gamma = gammas[best_test_index]
    best_avg_gamma = gammas[best_avg_index]

    return (best_train_gamma, best_test_gamma, best_avg_gamma)
'''