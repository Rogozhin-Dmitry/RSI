import pathlib

import tensorflow as tf

batch_size = 32
img_height = 300
img_width = 300

data_dir = pathlib.Path('rsds')
class_names = ['main_way', 'give_way', 'brick', 'stop_line', 'banned_stop', 'train']


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
