# -*- coding: utf-8 -*-
"""Fuel_efficiency.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19nGCTX4xUAG_zP21gapBld9yT7OYVCsQ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

import tensorflow as tf
from tensorflow import keras
from keras import layers

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('auto-mpg.csv')
df.head()

df.shape

df.info()

df.describe()

df['horsepower'].unique()

print(df.shape)
df = df[df['horsepower'] != '?']
print(df.shape)

df['horsepower'] = df['horsepower'].astype(int)
df.isnull().sum()

df.nunique()

# Select only numeric columns for correlation calculation
numeric_df = df.select_dtypes(include=['number'])

plt.subplots(figsize=(15, 5))
for i, col in enumerate(['cylinders', 'origin']):
    plt.subplot(1, 2, i+1)
    x = numeric_df.groupby(col).mean()['mpg']
    x.plot.bar()
    plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# This code is written by Hammad Rana

plt.figure(figsize=(8, 8))
sb.heatmap(numeric_df.corr() > 0.9,
        annot=True,
        cbar=False)
plt.show()

# This code is modified by Hammad Rana

df.drop('displacement',
        axis=1,
        inplace=True)

from sklearn.model_selection import train_test_split
features = df.drop(['mpg', 'car name'], axis=1)
target = df['mpg'].values

X_train, X_val, \
    Y_train, Y_val = train_test_split(features, target,
                                      test_size=0.2,
                                      random_state=22)
X_train.shape, X_val.shape

AUTO = tf.data.experimental.AUTOTUNE

train_ds = (
    tf.data.Dataset
    .from_tensor_slices((X_train, Y_train))
    .batch(32)
    .prefetch(AUTO)
)

val_ds = (
    tf.data.Dataset
    .from_tensor_slices((X_val, Y_val))
    .batch(32)
    .prefetch(AUTO)
)

model = keras.Sequential([
    layers.Dense(256, activation='relu', input_shape=[6]),
    layers.BatchNormalization(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.3),
    layers.BatchNormalization(),
    layers.Dense(1, activation='relu')
])

model.compile(
    loss='mae',
    optimizer='adam',
    metrics=['mape']
)

model.summary()

history = model.fit(train_ds,
                    epochs=50,
                    validation_data=val_ds)

history_df = pd.DataFrame(history.history)
history_df.head()

history_df.loc[:, ['loss', 'val_loss']].plot()
history_df.loc[:, ['mape', 'val_mape']].plot()
plt.show()