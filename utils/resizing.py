import os
import cv2

# from utils import resizing
SIZE = (128, 128)

def resizing_data(file_path, size=(128, 128)):
    count = 0
    for root, _, files in os.walk(file_path):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                image_path = os.path.join(root, file)
                image = cv2.imread(image_path)
                if image is None:
                    print(f'Skipping {image_path}, could not load the image')
                    continue

                resized_image = cv2.resize(image, size)
                cv2.imwrite(image_path, resized_image)
                count += 1
    print(f'{count} images successfully resized')