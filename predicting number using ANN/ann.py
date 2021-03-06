# -*- coding: utf-8 -*-
"""ANN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-c8R8L4ni3C1AbcSK3QqTMekDeT0ic2c
"""

import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_train.shape

x_train,x_test = x_train/255, x_test/255

model = tf.keras.Sequential([
                             tf.keras.layers.Flatten(input_shape = (28,28)),
                             tf.keras.layers.Dense(128, activation='relu'),
                             tf.keras.layers.Dropout(0.2),
                             tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics = ['accuracy']
              )

r = model.fit(x_train,y_train, validation_data=(x_test, y_test), epochs=10)

import matplotlib.pyplot as plt
plt.plot(r.history['loss'],label='loss')
plt.plot(r.history['accuracy'],label="accuracy")
plt.plot(r.history['val_loss'],label="val_loss")
plt.plot(r.history['val_accuracy'],label="val_accuracy")
plt.legend()

import numpy as np
p_test = model.predict(x_test).argmax(axis=1)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, p_test)

cm

mis_classified_idx = np.where(p_test != y_test)[0]
i = np.random.choice(mis_classified_idx)
plt.imshow(x_test[i])

