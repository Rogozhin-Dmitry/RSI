import pathlib

import tensorflow as tf

batch_size = 32
img_height = 180
img_width = 180
file_name = 'road_traffic'

data_dir = tf.keras.utils.get_file(file_name, untar=True)
data_dir = pathlib.Path(data_dir)
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
