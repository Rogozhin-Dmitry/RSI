import os

import cv2
from tensorflow import keras


def prepare_img(filepath):
    IMG_SIZE = 32  # 50 in txt-based
    img_array = cv2.imread(filepath)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape((1, 32, 32, 3))


model = keras.models.load_model('models\\my_model')
class_names = ['main_way', 'give_way', 'brick', 'train', 'banned_stop']


a = 'test'
b1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
for i in os.listdir(fr'{a}'):
    prediction = model.predict(prepare_img(fr'{a}/{i}'))[0].tolist()

    b1[prediction.index(max(prediction))] += 1
print(b1)

# a = 'brick'
# b1 = {0: 0, 1: 0, 2: 0}
# for i in os.listdir(fr'rsds/{a}')[:100]:
#     prediction = model.predict(prepare_img(fr'rsds/{a}/{i}'))[0].tolist()
#     b1[prediction.index(max(prediction))] += 1
#     print(1)
#
# a = 'give_way'
# b2 = {0: 0, 1: 0, 2: 0}
# for i in os.listdir(fr'rsds/{a}')[:100]:
#     prediction = model.predict(prepare_img(fr'rsds/{a}/{i}'))[0].tolist()
#     b2[prediction.index(max(prediction))] += 1
#     print(2)
#
# a = 'main_way'
# b3 = {0: 0, 1: 0, 2: 0}
# for i in os.listdir(fr'rsds/{a}')[:100]:
#     prediction = model.predict(prepare_img(fr'rsds/{a}/{i}'))[0].tolist()
#     b3[prediction.index(max(prediction))] += 1
#     print(3)
# print(b1, b2, b3)
