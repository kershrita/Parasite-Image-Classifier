import os
import shutil
from glob import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt

def split_images_by_shape(input_folder, output_folder_low, output_folder_high, threshold_width, threshold_height):
    # Iterate through each class folder
    for class_folder in os.listdir(input_folder):
        class_path = os.path.join(input_folder, class_folder)

        # Create output folders for low and high shapes
        output_folder_low_class = os.path.join(output_folder_low, class_folder)
        output_folder_high_class = os.path.join(output_folder_high, class_folder)

        os.makedirs(output_folder_low_class, exist_ok=True)
        os.makedirs(output_folder_high_class, exist_ok=True)

        # Iterate through each image in the class folder
        for image_name in os.listdir(class_path):
            image_path = os.path.join(class_path, image_name)

            # Read the image using OpenCV
            image = cv2.imread(image_path)

            # Check the shape of the image
            height, width, _ = image.shape

            # Determine whether the image has high or low shapes based on the dimensions
            if width > threshold_width and height > threshold_height:
                output_path = os.path.join(output_folder_high_class, image_name)
            else:
                output_path = os.path.join(output_folder_low_class, image_name)

            # Save the image to the appropriate output folder
            cv2.imwrite(output_path, image)
        print("Done!")


def image_equalization(img):
    # Calculate the cumulative distribution function (CDF)
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    # Create a dictionary for mapping the original pixel values to the equalized values
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    
    # Apply the equalization to the image using the CDF mapping
    equalized_image = cdf[image]

    return equalized_image