# Project Airavat - YOLOv11 Cone Detection
Team OutPulse | International Space Drone Competition (ISDC)

📌 Overview
Project Airavat is a YOLOv11-based model trained to detect cones used as markers in the International Space Drone Competition (ISDC). This repository contains the trained model, dataset, and scripts for training and real-time inference.

🚀 Features
YOLOv11-based cone detection model
Trained on a custom dataset with labeled images
Supports real-time and image-based inference
Includes training and utility scripts

📂 Repository Structure
```
📦 Project-Airavat  
 ┣ 📂 dataset/             # Dataset with images and labels  
 ┃ ┣ 📂 train/             # Training set (images & labels)  
 ┃ ┗ 📂 valid/             # Validation set (images & labels)  
 ┣ 📜 best.pt              # Trained YOLOv11 model weights  
 ┣ 📜 yolo11n.pt           # YOLOv11 model file  
 ┣ 📜 orange_cone.yaml     # Class label configuration  
 ┣ 📜 train.py             # Script to train the model  
 ┣ 📜 detect.py            # Script for image-based inference  
 ┣ 📜 detectStream.py      # Script for real-time detection  
 ┣ 📜 utils.py             # Utility functions
```


To run cone detection on an image:
```python detect.py --image path/to/image.jpg```

For real-time detection via webcam:
```python detectStream.py```
