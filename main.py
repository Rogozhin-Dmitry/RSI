import tensorflow as tf

from dataset import img_width, img_height, class_names, train_ds, val_ds

num_classes = len(class_names)
model = tf.keras.models.Sequential([
    tf.keras.layers.Rescaling(1. / 255, input_shape=(img_height, img_width, 3)),
    tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),  # слой свёртки 16 карт признаков 3 на 3
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),  # слой подвыборки 2 на 2
    tf.keras.layers.Dropout(0.25),  # слой регуляризации отключающий каждый 4 нейрон
    tf.keras.layers.Conv2D(128, 3, padding='same', activation='relu'),  # слой свёртки 32 карт признаков 3 на 3
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),  # слой подвыборки 2 на 2
    tf.keras.layers.Dropout(0.25),  # слой регуляризации отключающий каждый 4 нейрон
    tf.keras.layers.Conv2D(256, 3, padding='same', activation='relu'),  # слой свёртки 64 карт признаков 3 на 3
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),  # слой подвыборки 2 на 2
    tf.keras.layers.Dropout(0.25),  # слой регуляризации отключающий каждый 4 нейрон
    tf.keras.layers.Flatten(),  # преобразование из двумерного вида в плоский
    tf.keras.layers.Dense(1024, activation='relu'),  # полносвязный слой
    tf.keras.layers.Dropout(0.5),  # слой регуляризации отключающий каждый 2 нейрон
    tf.keras.layers.Dense(num_classes, activation='softmax')  # выходной слой
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

epochs = 25

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs,
    shuffle=True
)

model.save('models\\RSI_MODEL')
