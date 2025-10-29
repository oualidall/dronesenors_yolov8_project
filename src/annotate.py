from ultralytics import YOLO
import json
import cv2
import numpy as np
from pathlib import Path

def annotate_rgb_image(image_file):
    """
    Runs YOLOv8 inference on an image file object and returns annotations in a dictionary format.

    Args:
        image_file: A file-like object containing the image data (e.g., from google.colab.files.upload()).

    Returns:
        dict: A dictionary containing the annotation data.
    """
    try:
        model = YOLO('yolov8s.pt')
    except Exception as e:
        print(f"Error loading YOLO model: {e}")
        try:
            model = YOLO('/content/yolov8s.pt')
        except Exception as e_nested:
            print(f"Error loading YOLO model from /content/: {e_nested}")
            return {"error": "Could not load YOLO model."}

    try:
        image_data = image_file.read()
        np_arr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if img is None:
            return {"error": "Could not decode image."}
    except Exception as e:
        return {"error": f"Error reading or decoding image file: {e}"}

    try:
        results = model(img)  # Run inference on the image data
    except Exception as e:
        return {"error": f"Error during YOLO inference: {e}"}

    annotation_data = {}
    if results:
        r = results[0]
        if r.boxes is not None:
            objs = []
            for box in r.boxes:
                x_min, y_min, x_max, y_max = [float(coord) for coord in box.xyxy[0]]
                confidence = float(box.conf[0])
                class_id = int(box.cls[0])
                obj_name = "unknown"
                if 0 <= class_id < len(model.names):
                    obj_name = model.names[class_id]
                objs.append({
                    "contour": {"x": x_min, "y": y_min, "w": x_max - x_min, "h": y_max - y_min},
                    "obj_name": obj_name,
                    "name_accuracy": confidence
                })
            annotation_data["objects"] = objs
        else:
            annotation_data["objects"] = []

    image_filename = getattr(image_file, 'name', 'unknown_filename.jpg')
    return {
        "image_filename": Path(image_filename).name,
        "image_dimensions": {"width": int(img.shape[1]), "height": int(img.shape[0])},
        "objects": annotation_data.get("objects", [])
    }
