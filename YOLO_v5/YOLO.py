import cv2
import torch
import ipywidgets as widgets
from IPython.display import display
from io import BytesIO
from PIL import Image
from ultralytics import YOLO
import numpy as np

model = YOLO('runs/detect/train/weights/best.pt')

def detect_objects(image):
    # Convert PIL Image to numpy array
    img_np = np.array(image)

    # Perform object detection on the image
    results = model(img_np)

    # Display the results
    results.show()

def detect_objects_webcam():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to PIL Image
        img_pil = Image.fromarray(frame)

        # Perform object detection on the frame
        detect_objects(img_pil)

        # Exit the loop if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and destroy all windows
    cap.release()
    cv2.destroyAllWindows()    

def on_webcam_button_click(change):
    detect_objects_webcam()    


image_upload = widgets.FileUpload(accept='image/*', description='Upload Image')
webcam_button = widgets.Button(description='Detect Objects from Webcam')    

image_upload.observe(lambda change: detect_objects(list(change['new'].values())[0]['content']), names='value')
webcam_button.on_click(on_webcam_button_click)

# Display the widgets
display(image_upload)
display(webcam_button)
