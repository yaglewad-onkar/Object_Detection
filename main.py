import cv2
import concurrent.futures
from object_ident import getObjects
from web_server import app as flask_app
import threading

def object_detection():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        success, img = cap.read()
        result, objectInfo = getObjects(img, 0.45, 0.2)
        cv2.imshow("Output", img)
        cv2.waitKey(1)

def main():
    # Start the web server in a separate thread
    web_server_thread = threading.Thread(target=flask_app.run, kwargs={'host':'0.0.0.0', 'port':5000})
    web_server_thread.start()

    # Continue with the object detection code
    object_detection()

if __name__ == "__main__":
    main()
