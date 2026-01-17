import tensorflow as tf

def normalize_layers(data):
    normalize_layer = tf.keras.layers.Rescaling(1./255)
    data = data.map(lambda x, y: (normalize_layer(x), y))
    return data
