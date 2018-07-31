# Question: Write a XOR model to prevent the result of a XOR b
# Question: Write your own metrics, loss and optimizer
import tensorflow as tf
import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

class XOR(tf.keras.Model):
    def __init__(self):
        super(XOR, self).__init__(self)
        self.dense1 = tf.keras.layers.Dense(32, activation='relu')
        self.dense2 = tf.keras.layers.Dense(1, activation='sigmoid')

    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dense2(x)
        return x

def accuracy(y_true, y_pred):
    return tf.keras.metrics.binary_accuracy(y_true, y_pred)

def loss(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_pred - y_true), axis=-1)


class Optimizer(tf.keras.optimizers.Optimizer):

    def __init__(self, learning_rate):
        super(Optimizer, self).__init__()
        self._learning_rate = learning_rate


    def get_updates(self, loss, params):
        updates = []
        # TODO: Implement here
        grads = tf.gradients(loss, params)
        for p, q in zip(params, grads):
            v = self._learning_rate * q
            op = tf.assign_sub(p, v)
            updates.append(op)
        return updates

def run():
    m = XOR()
    m.compile(loss=loss, optimizer=Optimizer(learning_rate=0.11), metrics=[accuracy])
    m.fit(X, y, epochs=500)
    print(m.predict(X))

if __name__ == "__main__":
    run()
