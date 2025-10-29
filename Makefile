.PHONY: install frames annotate clean lint format

install:
	python -m pip install --upgrade pip
	# torch CPU (déjà OK chez toi, garde simple)
	pip install -r requirements.txt
	pip install black ruff

frames:
	python scripts/extract_frames.py data/videos data/frames_dataset 10

annotate:
	python scripts/annotate_batch.py data/frames_dataset annotations

clean:
	rm -f annotations/*.json
	rm -f data/frames_dataset/*.jpg

lint:
	ruff check .

format:
	black .
