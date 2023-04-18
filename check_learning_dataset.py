from tensorflow import keras

from dataset import train_ds, val_ds

model = keras.models.load_model('models\\my_model')

scores = model.evaluate(train_ds)
print('train_ds:', scores[1] * 100)

scores = model.evaluate(val_ds)
print('val_ds:', scores[1] * 100)
