import os
import cv2

# from utils import resizing
SIZE = (128, 128)

type_files = ['train', 'test', 'val']
classes = ['tumor', 'healthy']
base_path = r"C:\Users\Tony\PycharmProjects\BrainCancerDetection\data\split"

files = os.listdir(r"..\data\split")

def resizing_dataset():
    for file in type_files:
        for class_name in classes:
            for file_name in os.listdir(os.path.join(base_path,file, class_name)):
                if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
                    img_path = os.path.join(base_path, file, class_name, file_name)
                    img = cv2.imread(img_path)
                    if img is None:
                        print(f'Skipping {img_path}, could not load the image')
                        continue
                    resized_img = cv2.resize(img, SIZE)
                    cv2.imwrite(img_path, resized_img)
    print(f'{len(files)} images successfully resized')


def resizing_data(file_path):
    count = 0
    for file in os.listdir(file_path):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(file_path, file)
            image = cv2.imread(image_path)
            if image is None:
                print(f'Skipping {image_path}, could not load the image')
                continue

            resized_image = cv2.resize(image, SIZE)
            cv2.imwrite(image_path, resized_image)
            count += 1
    print(f'{count} images successfully resized')