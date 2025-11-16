import tensorflow as tf

saved_h5 = 'export/nilm_model.h5'
out_tflite = 'export/nilm_model.tflite'
model = tf.keras.models.load_model(saved_h5)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()
with open(out_tflite, 'wb') as f:
    f.write(tflite_model)
print("Wrote", out_tflite)
