"""Package drone_yolov8_project."""
from .annotate import annotate_rgb_image
from .utils import annotate_rgb_image as annotate_rgb_image_from_utils  # compat

__all__ = ["annotate_rgb_image", "annotate_rgb_image_from_utils"]
