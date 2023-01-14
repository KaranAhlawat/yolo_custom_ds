import os
from sklearn.model_selection import train_test_split
import shutil

def move_files_to_folder(list_of_files: list[str], destination_folder: str) -> None:
    for f in list_of_files:
        try:
            shutil.move(f, destination_folder)
        except:
            print(f)
            assert False

def main() -> None:
    images = [os.path.join('anomalies_data/base', x) for x in os.listdir('anomalies_data/base') if x[-3:] == "jpg"]
    annotations = [os.path.join('anomalies_data/base', x) for x in os.listdir('anomalies_data/base') if x[-3:] == "txt"]

    images.sort()
    annotations.sort()

    train_images, val_images, train_annots, val_annots = train_test_split(images, annotations, test_size=0.2)
    val_images, test_images, val_annots, test_annots = train_test_split(val_images, val_annots, test_size=0.5)

    # move_files_to_folder(train_images, 'anomalies_data/images/train')
    # move_files_to_folder(val_images, 'anomalies_data/images/val')
    # move_files_to_folder(test_images, 'anomalies_data/images/test')
    # move_files_to_folder(train_annots, 'anomalies_data/labels/train')
    # move_files_to_folder(val_annots, 'anomalies_data/labels/val')
    # move_files_to_folder(test_annots, 'anomalies_data/labels/test')

if __name__ == "__main__":
    main()


# python train.py --img-size 640 --cfg cfg/training/yolov7.yaml --hyp data/hyp.scratch.custom.yaml --batch 8 --epochs 100 --data data/anomalies_data.yaml --weights yolov7_training.pt --workers 24 --name yolo_road_det