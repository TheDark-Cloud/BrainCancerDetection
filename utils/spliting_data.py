import os, glob, shutil
from sklearn.model_selection import train_test_split
from src.data_loader import cfg

raw_data = cfg['data']['raw_data']
output = cfg['data']['split_data']

classes = os.listdir(raw_data)
for class_name in classes:
    images = glob.glob(os.path.join(raw_data, class_name, "*.jpg"))

    # splitting the dataset
    train_images, temp_images = train_test_split(images, test_size=0.2, random_state=42)
    test_images, val_images = train_test_split(temp_images, test_size=0.5, random_state=42)

    for splits, split_images in zip(['train', 'val', 'test'], [train_images, val_images, test_images]):
        split_dir = os.path.join(output, splits, class_name)
        os.makedirs(split_dir, exist_ok=True)
        for image in split_images:
            shutil.copy(image, split_dir)






