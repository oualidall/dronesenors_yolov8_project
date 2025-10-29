# -*- coding: utf-8 -*-

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
    # Load the model inside the function for simplicity in this standalone file,
    # or pass it as an argument if loading globally is preferred.
    # Assuming 'yolov8s.pt' is available in the current working directory or a specified path.
    try:
        model = YOLO('yolov8s.pt')
    except Exception as e:
        print(f"Error loading YOLO model: {e}")
        # Attempt to load from a common location if not found in cwd
        try:
             model = YOLO('/content/yolov8s.pt')
        except Exception as e_nested:
             print(f"Error loading YOLO model from /content/: {e_nested}")
             return {"error": "Could not load YOLO model."}


    # Read image data from the file object
    try:
        image_data = image_file.read()
        np_arr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if img is None:
            print("Error: Could not decode image.")
            return {"error": "Could not decode image."}
    except Exception as e:
        print(f"Error reading or decoding image file: {e}")
        return {"error": f"Error reading or decoding image file: {e}"}


    try:
        results = model(img)  # Run inference on the image data
    except Exception as e:
        print(f"Error during YOLO inference: {e}")
        return {"error": f"Error during YOLO inference: {e}"}


    annotation_data = {}

    if results: # Check if results list is not empty
      for i, r in enumerate(results):
          if r.boxes is not None:
              annotation_data[f"obj_{i+1}"] = []
              for box in r.boxes:
                  # Ensure coordinates are within image bounds and are floats
                  x_min, y_min, x_max, y_max = [float(coord) for coord in box.xyxy[0]]

                  # Optional: Clamp coordinates to image boundaries if necessary
                  # x_min = max(0, x_min)
                  # y_min = max(0, y_min)
                  # x_max = min(img.shape[1], x_max)
                  # y_max = min(img.shape[0], y_max)


                  confidence = float(box.conf[0])
                  class_id = int(box.cls[0])

                  # Handle cases where class_id might be out of bounds for model.names
                  obj_name = "unknown"
                  if 0 <= class_id < len(model.names):
                      obj_name = model.names[class_id]
                  else:
                      print(f"Warning: Class ID {class_id} out of bounds for model names.")


                  annotation_data[f"obj_{i+1}"].append({
                      "contour": {"x": x_min, "y": y_min, "w": x_max - x_min, "h": y_max - y_min},
                      "obj_name": obj_name,
                      "name_accuracy": confidence
                  })
          # Handle cases where r.boxes might be None or results list is empty
          elif results[0].boxes is None and len(results[0]) == 0:
              print("No objects detected in the image.")
              # You might want to return an empty object list or a specific message
              return {"image_filename": "N/A", # Cannot get filename from file object easily here
                      "image_dimensions": {"width": img.shape[1], "height": img.shape[0]},
                      "objects": []}

    # Add image dimensions and filename to the annotation data
    # Note: Getting the original filename from a file object is not straightforward.
    # You might need to pass the filename as an argument to the function.
    # For now, we'll use a placeholder or try to get from the file object if possible.
    image_filename = getattr(image_file, 'name', 'unknown_filename.jpg') # Try to get name attribute
    annotation_data = {
        "image_filename": Path(image_filename).name, # Use just the filename
        "image_dimensions": {
            "width": int(img.shape[1]),
            "height": int(img.shape[0])
        },
        "objects": annotation_data.get("obj_1", []) # Assuming only one result object for now
    }


    return annotation_data

