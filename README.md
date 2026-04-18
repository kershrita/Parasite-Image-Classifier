# Parasite Image Classification System

End-to-end medical computer vision system for parasite microscopy image analysis, combining multi-class classification and an optional object detection branch for localization and crop-based workflows.

![Parasite Samples](assets/Custom%20CNN/Custom%20CNN%20-%20Samples.jpg)

## Overview

This project was built as an applied AI engineering system, not only a model training exercise. It is designed to support practical microscopy analysis where speed, repeatability, and clear evaluation are critical.

The initial project context was participation in the IEEE MANSB Victoris 2 Final Competition hosted on Kaggle, then extension into a broader end-to-end AI workflow.

The system addresses the problem of manual parasite identification by providing:

- Structured image preprocessing and augmentation to improve robustness.
- Multi-architecture classification experiments (Custom CNN and transfer learning models).
- Optional YOLOv8-based detection pipeline for parasite localization and crop generation.
- Evaluation artifacts for model comparison and operational decision-making.

Real-world use cases:

- Laboratory screening support and triage assistance.
- Research workflows for parasite species analysis at scale.
- Educational and clinical prototyping for AI-assisted diagnostics.

## Architecture

The platform follows a staged ML system design:

1. Input Layer: Microscopy images from curated parasite datasets.
2. Processing Layer: Data cleaning, resizing, augmentation, and dataset balancing.
3. Modeling Layer: Classification training (Custom CNN, ResNet50, ResNet50V2, Xception) and optional YOLOv8 detection.
4. Evaluation Layer: History curves, confusion matrices, AUC plots, and detection metrics.
5. Inference Layer: Class prediction and optional object-level crop extraction.

System flow:

`Microscopy Images -> Preprocessing/Augmentation -> Model Training -> Evaluation -> Inference Outputs`

### Architecture Diagram

The repository now includes the architecture diagram used for this staged ML flow:

![Staged ML System Flow for Parasite Image Analysis](assets/Staged%20ML%20System%20Flow%20for%20Parasite%20Image%20Analysis.png)


## Features

- Multi-class parasite image classification across 21 labeled classes.
- Transfer learning support using ResNet50, ResNet50V2, and Xception.
- Custom CNN baseline for architecture comparison.
- Preprocessing and augmentation workflow to improve generalization.
- YOLOv8 detection extension for object localization and crop extraction.
- Experiment artifacts for each model family (history, AUC, confusion matrix, samples).
- Notebook-first reproducible workflow from preparation to inference.

## Dataset Sources and Label Taxonomy

Dataset sources used across the original workflow:

- [IEEE DataPort - Parasitic Egg Detection and Classification](https://ieee-dataport.org/competitions/parasitic-egg-detection-and-classification-microscopic-images)
- [Kaggle - Parasite Dataset](https://www.kaggle.com/datasets/redrik278/parasite-dataset)

Primary classification label mapping (21 classes):

| Label | Description |
|---:|---|
| 0 | Ascariasis |
| 1 | Babesia |
| 2 | Capillaria philippinensis |
| 3 | Enterobius vermicularis |
| 4 | Epidermophyton floccosum |
| 5 | Fasciolopsis buski |
| 6 | Hookworm egg |
| 7 | Hymenolepis diminuta |
| 8 | Hymenolepis nana |
| 9 | Leishmania |
| 10 | Leukocyte 400X |
| 11 | Leukocyte 1000X |
| 12 | Opisthorchis viverrine |
| 13 | Paragonimus spp |
| 14 | Plasmodium |
| 15 | Trichophyton rubrum (T. rubrum) |
| 16 | Taenia spp |
| 17 | Toxoplasma |
| 18 | Trichomonad |
| 19 | Trichuris trichiura |
| 20 | Trypanosome |

## Technical Highlights

- Designed as a full pipeline from data preparation to inference, not a single notebook experiment.
- Used transfer learning as a deliberate design choice to improve sample efficiency on specialized medical imagery.
- Maintained both classification and detection capabilities to support multiple operational modes.
- Preserved evaluation transparency through architecture-specific visual diagnostics stored in-repo.
- Structured code and notebooks to support extension into API-based or cloud-based serving.

## Model Details

- Baseline model: Custom CNN for controlled comparison.
- Transfer models: ResNet50, ResNet50V2, Xception.
- Detection model: YOLOv8 (custom dataset training in `parasite detection/TrainYolov8CustomDataset.ipynb`).
- Evaluation approach:
	- Classification: confusion matrix, AUC, training history, sample predictions.
	- Detection: precision, recall, mAP@50, mAP@50-95 tracked per epoch.

## Tech Stack

- Language: Python
- Notebooks: Jupyter
- Deep Learning: TensorFlow/Keras, PyTorch
- Computer Vision: OpenCV, Ultralytics YOLOv8
- Data and Analysis: NumPy, pandas, scikit-learn, Matplotlib
- Experiment Tracking: TensorBoard logs (YOLO training runs)
- Cloud Readiness: Microsoft Azure / Azure Machine Learning (integration-ready workflow)

## Skills Demonstrated

- Data preprocessing, feature engineering, and dataset balancing.
- Computer vision and image processing with OpenCV.
- Transfer learning and deep learning model development.
- Classification modeling and predictive analytics.
- Data analysis with NumPy and pandas.
- Statistics-driven model evaluation and reporting.
- API design mindset for downstream integration.
- Cloud-aligned ML workflows (Azure and Azure ML readiness).

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- Jupyter Notebook or VS Code with Jupyter extension

### Installation

```bash
git clone https://github.com/<your-username>/Parasite-Image-Classifier.git
cd Parasite-Image-Classifier
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install jupyter numpy pandas matplotlib scikit-learn opencv-python tensorflow torch torchvision ultralytics
```

### Run the Classification Workflow

Open notebooks in this sequence:

1. `1 - Perpare Data.ipynb`
2. `2 - Data Anaylsis.ipynb`
3. `3 - Deep Learning Model.ipynb`
4. `4 - Transfer Learning.ipynb`
5. `5 - Parasite Image Classifier.ipynb`

```bash
jupyter notebook
```

### Run the Detection Workflow

- Training notebook: `parasite detection/TrainYolov8CustomDataset.ipynb`
- Inference notebook: `parasite detection/Detection.ipynb`
- Detection utility class: `parasite detection/Main.py`
- Trained weights examples:
	- `parasite detection/train/80-epochs/weights/best.pt`
	- `parasite detection/train/200-epochs/weights/best.pt`

## Results

### Classification Artifacts

The repository includes architecture-level evaluation outputs under:

- `assets/Custom CNN`
- `assets/ResNet50`
- `assets/ResNet50V2`
- `assets/Xception`

Each folder contains model history, confusion matrix, AUC, and sample output visuals for technical review.

### Detection Benchmarks (YOLOv8)

Metrics extracted from tracked training logs:

| Run | Best mAP@50 | Epoch | Best mAP@50-95 | Epoch | Final Precision | Final Recall | Final mAP@50 | Final mAP@50-95 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 80 epochs | 0.97071 | 47 | 0.81999 | 47 | 0.87429 | 0.89445 | 0.93801 | 0.79261 |
| 200 epochs | 0.99442 | 90 | 0.84442 | 90 | 0.93633 | 0.90635 | 0.93236 | 0.76508 |

Engineering interpretation:

- Longer training improved peak mAP performance.
- Final-epoch drop in mAP@50-95 on the 200-epoch run suggests monitoring for overfitting and selecting weights by validation best epoch, not final epoch.
