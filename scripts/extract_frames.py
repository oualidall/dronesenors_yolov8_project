import cv2
import sys
from pathlib import Path

def extract_frames(video_dir, output_dir, every_n=10):
    video_dir, output_dir = Path(video_dir), Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    videos = list(video_dir.glob("*.mp4"))
    if not videos:
        print(f"[!] No .mp4 videos found in {video_dir}")
        return

    for video_file in videos:
        cap = cv2.VideoCapture(str(video_file))
        if not cap.isOpened():
            print(f"[x] Unable to open {video_file}")
            continue

        frame_count = 0
        saved_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count % every_n == 0:
                frame_name = f"{video_file.stem}_frame{saved_count:04d}.jpg"
                cv2.imwrite(str(output_dir / frame_name), frame)
                saved_count += 1
            frame_count += 1
        cap.release()
        print(f"[✓] {video_file.name} -> {saved_count} frames (stride={every_n})")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/extract_frames.py <video_dir> <output_dir> [every_n]")
        sys.exit(1)
    video_dir, output_dir = sys.argv[1], sys.argv[2]
    every_n = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    extract_frames(video_dir, output_dir, every_n)
