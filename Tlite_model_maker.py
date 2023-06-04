import tensorflow as tf
import pathlib


converter = tf.lite.TFLiteConverter.from_saved_model('models\\RSI_MODEL')
tflite_model = converter.convert()
tflite_model_file = pathlib.Path('models\\RSI.tflite')
tflite_model_file.write_bytes(tflite_model)

interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
print(input_details)
print(output_details)
