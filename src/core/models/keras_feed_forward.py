from src.core import DataManager
from keras.models import Sequential
from keras.layers import Dense
from keras import metrics

dm = DataManager("data/train.csv")
dm.tokenize()

input_shape = dm.dat['tokenized'].as_matrix().shape


model = Sequential()
model.add(Dense(128, activation="relu", input_shape=input_shape))
model.add(Dense(64, activation="relu"))
model.add(Dense(16, activation="relu"))
model.add(Dense(2, activation='softmax'))


model.compile(optimizer="adam", loss='categorical_crossentropy',
              metrics=[metrics.categorical_accuracy, metrics.mae])

