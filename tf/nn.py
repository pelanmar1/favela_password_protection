'''
A Multilayer Perceptron implementation example using TensorFlow library.
This example is using the MNIST database of handwritten digits
(http://yann.lecun.com/exdb/mnist/)

Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

from __future__ import print_function
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
#mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

import tensorflow as tf



# input data

def createPassTrainData():
    x_path = '../rnd_test.csv'
    dataset = pd.read_csv(x_path,header=-1)
    X = dataset.values
    
    Y = np.zeros((X.shape[0],2))
    for i in range(X.shape[0]):
        if i < 18:
            Y[i] = [1,0]
        else:
            Y[i] = [0,1]
    
    
    return (X,Y)

def createPassTestData():
    x_path = '../real_test.csv'
    dataset = pd.read_csv(x_path,header=-1)
    X = dataset.values
    return X
    

X,Y = createPassTrainData()

X_test = createPassTestData()

num_samples = len(X)

# Parameters
learning_rate = 0.001
training_epochs = 1000
batch_size = 1
display_step = 1

# Network Parameters
n_hidden_1 = 8 # 1st layer number of features
n_hidden_2 = 8 # 2nd layer number of features
n_input = 8 # MNIST data input (img shape: 28*28)
n_classes = 2 # MNIST total classes (0-9 digits)

# tf Graph input
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])


def multilayer_perceptron(x, weights, biases):
    # Hidden layer with RELU activation
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # Hidden layer with RELU activation
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    # Output layer with linear activation
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# Construct model
pred = multilayer_perceptron(x, weights, biases)

# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# Initializing the variables
init = tf.global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(num_samples/batch_size)
        # Loop over all batches
        for i in range(total_batch):
            batch_x, batch_y = X,Y
            # Run optimization op (backprop) and cost op (to get loss value)
            _, c = sess.run([optimizer, cost], feed_dict={x: batch_x,
                                                          y: batch_y})
            # Compute average loss
            avg_cost += c / total_batch
        # Display logs per epoch step
        if epoch % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", \
                "{:.9f}".format(avg_cost))
    print("Optimization Finished!")

    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    #print("Accuracy:", accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))
    result = sess.run(pred, feed_dict={x:X_test })
    filtered = []
    for a in result:
        tmp = []
        for x in a:
            if x > 0:
                tmp.append(1)
            else:
                tmp.append(0)
        filtered.append(tmp)
    for i in range(len(filtered)):
        print(str(i)+" - "+str(filtered[i]))
    
    
def createTestData():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = pd.read_csv(url, names=names)
    
    y_names = dataset['class'].unique()
    
    le = preprocessing.LabelEncoder()
    
    le.fit(y_names)
    y_vals = le.transform(dataset['class'].values)
    dataset['class'] = y_values
    X = dataset[dataset.columns[:-1]].values
    Y = dataset[dataset.columns[-1]].values
    
    x, x_test, y, y_test = train_test_split(X,Y,test_size=0.2,train_size=0.8)
    
    return (X,Y)


    
    

