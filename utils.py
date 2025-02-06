import cv2


def get_csi_camera():
    return cv2.VideoCapture(
        "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=30/1 ! "
        "nvvidconv flip-method=0 ! video/x-raw, width=640, height=480, format=BGRx ! "
        "videoconvert ! video/x-raw, format=BGR ! appsink",
        cv2.CAP_GSTREAMER
    )