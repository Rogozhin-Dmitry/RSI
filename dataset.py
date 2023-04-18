import pathlib

import tensorflow as tf

batch_size = 32
img_height = 32
img_width = 32
file_name = r'rsds'

data_dir = pathlib.Path(file_name)
# class_names = ['main_way', 'give_way', 'brick', 'stop_line', 'banned_stop', 'train']
class_names = ['main_way', 'give_way', 'brick', 'train', 'banned_stop']


train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)
