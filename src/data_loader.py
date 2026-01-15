from tensorflow.keras.utils import image_dataset_from_directory
import yaml, os

with open(r'..\config.yaml', 'r') as config_yaml:
    cfg = yaml.load(config_yaml, Loader=yaml.FullLoader)

img_size = cfg['image']['image_size']
batch_size = cfg['image']['batch_size']

def load_data(base_path) -> tuple:
    train_datagen = image_dataset_from_directory(
        os.path.join(base_path, "train"),
        image_size=img_size,
        shuffle=True,
        batch_size=batch_size
    )

    test_datagen = image_dataset_from_directory(
        os.path.join(base_path, "test"),
        image_size=img_size,
        shuffle=True,
        batch_size=batch_size
    )
    val_datagen = image_dataset_from_directory(
        os.path.join(base_path, "val"),
        image_size=img_size,
        shuffle=True,
        batch_size=batch_size
    )
    return train_datagen, test_datagen, val_datagen