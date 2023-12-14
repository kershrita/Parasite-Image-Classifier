import os
from ultralytics import YOLO
import cv2

class ParasiteDetector:
    def __init__(self, model_path, threshold):
        self.model = YOLO(model_path)
        self.threshold = threshold

    def detect_parasites(self, image_path, output_path):
        image_files = [f for f in os.listdir(image_path) if f.endswith('.jpg')]

        for image_file in image_files:
            inimg = os.path.join(image_path, image_file)
            outimg = os.path.join(output_path, image_file)

            image = cv2.imread(inimg)
            H, W, _ = image.shape

            results = self.model(image)[0]

            for result in results.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = result

                if score > self.threshold:
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                    cv2.putText(image, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            cv2.imwrite(outimg, image)
            print(f"{image_file} Done!")

    def crop_parasites(self, image_path, output_path):
        image_files = [f for f in os.listdir(image_path) if f.endswith('.jpg')]

        for image_file in image_files:
            inimg = os.path.join(image_path, image_file)
            outimg = os.path.join(output_path, image_file)

            image = cv2.imread(inimg)
            H, W, _ = image.shape

            results = self.model(image)[0]

            for result in results.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = result

                if score > self.threshold:
                    # Crop the detected parasite
                    cropped_parasite = image[int(y1):int(y2), int(x1):int(x2)]
                    cv2.imwrite(outimg, cropped_parasite)
                    print(f"{image_file} Cropped and Saved!")