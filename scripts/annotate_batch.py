import json
import sys
from pathlib import Path
from src.annotate import annotate_rgb_image

def annotate_folder(image_dir, output_dir):
    image_dir, output_dir = Path(image_dir), Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    images = []
    for ext in ("*.jpg","*.jpeg","*.png"):
        images.extend(image_dir.glob(ext))
    if not images:
        print(f"[!] No images found in {image_dir}")
        return

    for img_path in images:
        with open(img_path, "rb") as f:
            ann = annotate_rgb_image(f)
        out_path = output_dir / f"{img_path.stem}.json"
        with open(out_path, "w") as out:
            json.dump(ann, out, indent=2)
        print(f"[✓] {img_path.name} -> {out_path.name}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/annotate_batch.py <image_dir> <output_dir>")
        sys.exit(1)
    annotate_folder(sys.argv[1], sys.argv[2])
