import cv2
import concurrent.futures
from object_ident import getObjects  # Adjust the import statement
from web_server import run_web_server

def main():
    # Start the web server in a separate thread
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(run_web_server)

    # Continue with the object detection code
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        success, img = cap.read()
        result, objectInfo = getObjects(img, 0.45, 0.2)
        # print(objectInfo)
        cv2.imshow("Output", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()