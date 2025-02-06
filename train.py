from torch.xpu import device
from ultralytics import YOLO

model = YOLO('yolo11n.pt')  # Ensure 'yolo11n.pt' is the correct model file

model.train(
    data='orange_cone.yaml',  # Ensure this YAML file is correctly configured for your dataset
    epochs=100,
    imgsz=320,
    device='cpu',  # Use 'cpu' or 'cuda' depending on your hardware
    batch=16
)

model.export(format="onnx", device='cpu')