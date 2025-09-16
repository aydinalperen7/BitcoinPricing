# %% visualize the bicoin prizes over the years

# %% visualize the bicoin prizes over the years

import numpy as np
import matplotlib.pyplot as plt
import csv
from numpy import array
from numpy import hstack
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from tqdm import tqdm
import pandas as pd
import keras

# %% 

filename = 'BTC-USD.csv'


dates = []
opens = []
highs = []
lows = []
closes = []
adj_closes = []
volumes = []

with open(filename, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        dates.append(row[0])
        opens.append(float(row[1]))
        highs.append(float(row[2]))
        lows.append(float(row[3]))
        closes.append(float(row[4]))
        adj_closes.append(float(row[5]))
        volumes.append(int(row[6]))

percentage_changes = [(volumes[i] - volumes[i - 1]) / volumes[i - 1] * 100 if i > 0 else None for i in range(len(volumes))]

# %% 
def calculate_moving_average(prices, days):
    moving_averages = []
    for i in range(len(prices)):
        if i + 1 < days:
            moving_averages.append(None)  # Not enough data to calculate
        else:
            window = prices[i + 1 - days:i + 1]
            moving_average = sum(window) / days
            moving_averages.append(moving_average)
    return moving_averages


close_series = pd.Series(closes)

percent_change_7d = close_series.pct_change(periods=7) * 100
percent_change_30d = close_series.pct_change(periods=30) * 100
percent_change_60d = close_series.pct_change(periods=60) * 100

# Convert percent change series to numpy arrays and reshape them
percent_change_7d = percent_change_7d.values.reshape((-1, 1))
percent_change_30d = percent_change_30d.values.reshape((-1, 1))
percent_change_60d = percent_change_60d.values.reshape((-1, 1))

# %% Load the data from the CSV

mv_avg_data = (np.array(highs) + np.array(lows)) / 2

five_day_ma = calculate_moving_average(mv_avg_data, 5)
ten_day_ma = calculate_moving_average(mv_avg_data, 10)

five_day_ma_volume = calculate_moving_average(volumes, 5)
ten_day_ma_volume = calculate_moving_average(volumes, 10)

out_seq2 = np.array(closes).reshape((len(closes), 1))

out_seq_shifted = np.roll(out_seq2, shift=1, axis=0)
out_seq_shifted[0] = np.nan

in_seq1 = np.array(highs).reshape((len(highs), 1))
in_seq2 = np.array(lows).reshape((len(highs), 1))
in_seq3 = np.array(opens).reshape((len(highs), 1))
in_seq4 = np.array(volumes).reshape((len(highs), 1))
in_seq5 = np.array(five_day_ma).reshape((len(five_day_ma), 1))
in_seq6 = np.array(ten_day_ma).reshape((len(ten_day_ma), 1))
in_seq7 = np.array(five_day_ma_volume).reshape((len(five_day_ma_volume), 1))
in_seq8 = np.array(ten_day_ma_volume).reshape((len(ten_day_ma_volume), 1))
in_seq9 = np.array(percentage_changes).reshape((len(percentage_changes), 1))
in_seq10 = np.array(out_seq_shifted).reshape((len(out_seq_shifted), 1))
in_seq11 = np.array(percent_change_7d).reshape((len(percent_change_7d), 1))
in_seq12 = np.array(percent_change_30d).reshape((len(percent_change_30d), 1))
in_seq13 = np.array(percent_change_60d).reshape((len(percent_change_60d), 1))


out_seq = np.array(closes).reshape((len(highs), 1))

# horizontally stack columns
dataset = hstack((in_seq1, in_seq2, in_seq3, in_seq4, out_seq))
in_seq5 = in_seq5.astype(np.float64)
in_seq6 = in_seq6.astype(np.float64)
in_seq7 = in_seq7.astype(np.float64)
in_seq8 = in_seq8.astype(np.float64)
in_seq9 = in_seq9.astype(np.float64)
in_seq10 = in_seq10.astype(np.float64)




start_day = 60
# horizontally stack columns
dataset = hstack((in_seq1[start_day:], in_seq2[start_day:], in_seq3[start_day:], in_seq4[start_day:],in_seq5[start_day:], in_seq6[start_day:],in_seq9[start_day:],in_seq10[start_day:],in_seq11[start_day:],in_seq12[start_day:],in_seq13[start_day:] ,out_seq[start_day:]))

print(dataset)

# %% data set scaler

from sklearn.model_selection import train_test_split

dmax = np.max(dataset, axis=0)

dataset_train, dataset_test = train_test_split(dataset,
                                               test_size=0.25,
                                               random_state=42, shuffle=False)

dataset_scaled_train = dataset_train/dmax
dataset_scaled_test = dataset_test/dmax

#datalow = np.min(dataset, axis = 0 )
#datahigh = np.max(dataset, axis = 0 )

#dataset_scaled_train = hstack((in_seq1[:len(in_seq1)*3//4]/datahigh[0],
#                               in_seq2[:len(in_seq1)*3//4]/datahigh[1],
#                               in_seq3[:len(in_seq1)*3//4]/datahigh[2],
#                               in_seq4[:len(in_seq1)*3//4]/datahigh[3],
#                               out_seq[:len(in_seq1)*3//4]/datahigh[4]))

#dataset_scaled_test = hstack((in_seq1[-len(in_seq1)//4:]/datahigh[0],
#                              in_seq2[-len(in_seq1)//4:]/datahigh[1],
#                              in_seq3[-len(in_seq1)//4:]/datahigh[2],
#                              in_seq4[-len(in_seq1)//4:]/datahigh[3],
#                              out_seq[-len(in_seq1)//4:]/datahigh[4]))


# %%
def split_sequences(sequences, n_steps):
    X, y = list(), list()
    for i in range(len(sequences)):
        # find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the dataset
        if end_ix >= len(sequences):
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix, -1]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)


# choose a number of time steps
n_steps = 3
# convert into input/output
X, y = split_sequences(dataset_scaled_train, n_steps)
# the dataset knows the number of features, e.g. 2

print(X, y)

# %%

n_features = X.shape[2]
print(n_features)

# define model
model = Sequential()
model.add(LSTM(25,
               activation='tanh',
               dropout = 0.25,
               kernel_regularizer = keras.regularizers.L1L2(l1 = 1e-5, l2 = 1e-4),
               bias_regularizer = keras.regularizers.L1L2(l1 = 1e-5, l2 = 1e-4),
               activity_regularizer = keras.regularizers.L1L2(l1 = 1e-5, l2 = 1e-4),
               input_shape=(n_steps,n_features),
               return_sequences=True))
model.add(LSTM(25,
               activation='relu',
               dropout = 0.25,
               kernel_regularizer = keras.regularizers.L1L2(l1 = 1e-5, l2 = 1e-4),
               bias_regularizer = keras.regularizers.L1L2(l1 = 1e-5, l2 = 1e-4),
               activity_regularizer = keras.regularizers.L1L2(l1 = 1e-5, l2 = 1e-4),
               input_shape=(n_steps,n_features),
               return_sequences=True))
#model.add(keras.layers.Dropout(0.2))
#model.add(Dense(5))
model.add(keras.layers.Dropout(0.2))
model.add(Dense(1))

print(model.summary())

# %%  BURA

import keras 
# fit model

nb_epoch = 1000
opt = keras.optimizers.Adadelta(learning_rate=1e-3)
model.compile(loss='mean_squared_error',
               optimizer=opt, metrics=['mse'])

val_loss_arr = []
train_loss_arr = [] 

for i in tqdm(range(nb_epoch)):
    history = model.fit(X,
               y,
                 epochs=1,
                   batch_size=100,
                     verbose=2,
                       shuffle=True, 
                        validation_split=0.1)
    #64

    val_loss_arr.append(history.history['val_loss'])
    train_loss_arr.append(history.history['loss'])
    
    #print(model.predict(X))
    model.reset_metrics()

    
# model.save("bitcoin_model_demo3.keras")

# %% plot losses 

plt.figure()
plt.subplot(1,3,1)
plt.plot(val_loss_arr)
plt.subplot(1,3,2)
plt.plot(train_loss_arr)
plt.subplot(1,3,3)
plt.semilogy(val_loss_arr)
plt.semilogy(train_loss_arr)



# %%

# %% demonstrate prediction
y_pred = []
y_truth = []

test_len  = dataset_scaled_test.shape[0]

for i in tqdm(range(test_len -n_steps)):

    x_input = dataset_scaled_test[i:i+n_steps, :]
    x_input = x_input.reshape((1, n_steps, n_features))
    yhat = model.predict(x_input, verbose=0)
    y_pred.append(yhat[0,0]*dmax[-1])
    y_truth.append(dataset_scaled_test[i+n_steps, -1]*dmax[-1])
# %%

plt.subplot(1,3,1)
plt.plot(y_pred)
plt.subplot(1,3,2)
plt.plot(y_truth)
plt.subplot(1,3,3)
plt.plot(y_truth)
plt.plot(y_pred)


# %%