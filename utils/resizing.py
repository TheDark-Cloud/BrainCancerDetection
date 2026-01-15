import os
import cv2

def resizing_data(files, width, height):
    for file in os.listdir(files):
        if file.endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(files, file)
            image = cv2.imread(img_path)

            if image is None:
                print(f'Skipping {img_path}, could not load image')
                continue

            resized_image = cv2.resize(image, (width, height))
            cv2.imwrite(img_path, resized_image)
