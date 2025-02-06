import cv2
from ultralytics import YOLO

def main():
    # Load YOLO model (Ensure the path is correct)
    model_path = r"jupyter/airavat/yolov11ConeModel/best.pt"
    model = YOLO(model_path)

    video_path = r"..."  # Change this to your video file path
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)

    output_path = r"..." # change this to the output path you want
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("End of video or failed to grab frame")
            break

        # Run YOLO object detection
        results = model(frame, conf=0.7, classes=[0])

        # Get the annotated frame with bounding boxes
        annotated_frame = results[0].plot()

        out.write(annotated_frame)

        resized_frame = cv2.resize(annotated_frame, (640, 640))

        # Display the frame
        cv2.imshow("YOLO Object Detection", resized_frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()