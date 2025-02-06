import cv2
from ultralytics import YOLO

def main():
    model_path = r"jupyter/airavat/yolov11ConeModel/best.pt"
    model = YOLO(model_path)

    cap = cv2.VideoCapture(0)

    cap.set(3, 1280)  # Width
    cap.set(4, 720)   # Height

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        results = model(frame, conf=0.7, classes=[0])

        annotated_frame = results[0].plot()

        resized_frame = cv2.resize(annotated_frame, (640, 640))  # Adjust size as needed

        cv2.imshow("YOLO Object Detection", resized_frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
