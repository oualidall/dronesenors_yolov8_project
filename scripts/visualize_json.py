import json, sys
from pathlib import Path
from PIL import Image, ImageDraw

def draw(img_path, json_path, out_path):
    img = Image.open(img_path).convert("RGB")
    W, H = img.size
    with open(json_path, "r") as f:
        data = json.load(f)
    objs = data.get("objects", [])
    draw = ImageDraw.Draw(img)

    for o in objs:
        c = o["contour"]
        # JSON = x,y,w,h  →  boîtes xyxy
        x1, y1 = float(c["x"]), float(c["y"])
        x2, y2 = x1 + float(c["w"]), y1 + float(c["h"])
        # clamp aux bords image
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(W-1, x2), min(H-1, y2)
        # dessiner boîte + étiquette
        draw.rectangle([x1, y1, x2, y2], outline="white", width=3)
        label = f'{o.get("obj_name","?")} {o.get("name_accuracy",0):.2f}'
        # bande noire derrière le texte
        tw = draw.textlength(label)
        th = 14
        pad = 6
        draw.rectangle([x1, y1 - (th + pad), x1 + tw + 2*pad, y1], fill="black")
        draw.text((x1 + pad, y1 - th - 1), label, fill="white")

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, quality=95)
    print(f"[✓] écrit -> {out_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python scripts/visualize_json.py <image.jpg> <labels.json> <out.jpg>")
        sys.exit(1)
    draw(sys.argv[1], sys.argv[2], sys.argv[3])
