import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
# placeholder: replace with real dataset
def load_dataset():
    # X: (N, features), y: (N, n_classes)
    X = np.random.randn(1000, 68).astype('float32')
    y = np.random.randint(0,2,size=(1000,4)).astype('float32')
    return X, y

def build_model(input_dim, n_classes):
    inp = layers.Input(shape=(input_dim,))
    x = layers.Dense(64, activation='relu')(inp)
    x = layers.Dense(32, activation='relu')(x)
    out = layers.Dense(n_classes, activation='softmax')(x)
    m = models.Model(inp, out)
    m.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return m

if __name__ == "__main__":
    X, y = load_dataset()
    model = build_model(X.shape[1], y.shape[1])
    model.fit(X, y, epochs=5, batch_size=32, validation_split=0.1)
    model.save('export/nilm_model.h5')
