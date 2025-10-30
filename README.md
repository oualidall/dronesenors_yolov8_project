![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-4.12.0-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
# 🛰️ DroneSensors YOLOv8 Project
**Auteur :** Oualid Allouch  
**Entreprise :** VTEC Lasers & Sensors Ltd. (Eindhoven, NL)  
**Rôle :** AI & Computer Vision Intern — Juin–Août 2025  

<p align="center">
  <img src="docs/pipeline_overview.png" alt="YOLOv8 Drone Pipeline" width="700"/>
</p>





## 🎯 Objectif

Pipeline IA de bout en bout pour l’analyse de **vidéos de drones** en **surveillance environnementale** :

- Extraction automatique de frames depuis des vidéos,  
- Détection & annotation avec **YOLOv8** (Ultralytics),  
- Export des résultats au format **JSON** (prêt pour l’entraînement ou l’évaluation).

---

## 📦 Structure

```bash
drone_yolov8_project/
├── src/
│   ├── annotate.py        # fonction d’inférence/annotation YOLOv8
│   ├── utils.py           # ré-export utilitaire
│   └── __init__.py
├── scripts/
│   ├── extract_frames.py  # extraction de frames depuis .mp4
│   └── annotate_batch.py  # annotation en batch -> JSON
├── data/
│   └── samples/           # quelques images d’exemple (légères)
├── annotations/
│   └── examples/          # quelques JSON d’exemple
├── results/               # résultats, logs (vide par défaut)
├── Makefile               # commandes pratiques
├── requirements.txt
└── README.md

## ⚙️ Installation rapide

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

---

## 🎯 Exemple d’annotation YOLOv8

| Image originale | Image annotée |
|:----------------:|:--------------:|
| ![Original](docs/original_frame.jpg) | ![Annotée](docs/example_annotation.jpg) |

<p align="center">
  <em>Comparaison avant/après : détection automatique d’objets sur la frame <code>video2.mp4_frame0156.jpg</code>.</em>
</p>

---

## 📄 Exemple d’annotation JSON

```json
{
  "image_filename": "video2.mp4_frame0156.jpg",
  "image_dimensions": { "width": 848, "height": 480 },
  "objects": [
    {
      "contour": { "x": 692.77, "y": 300.01, "w": 53.49, "h": 32.49 },
      "obj_name": "car",
      "name_accuracy": 0.7056
    },
    {
      "contour": { "x": 559.83, "y": 281.91, "w": 40.72, "h": 19.37 },
      "obj_name": "car",
      "name_accuracy": 0.6810
    },
    {
      "contour": { "x": 718.60, "y": 275.97, "w": 28.55, "h": 14.71 },
      "obj_name": "car",
      "name_accuracy": 0.4981
    },
    {
      "contour": { "x": 381.34, "y": 277.32, "w": 9.75, "h": 21.29 },
      "obj_name": "person",
      "name_accuracy": 0.3576
    }
  ]
}




## 🔗 Contact

👨‍💻 **Oualid Allouch**  
AI & Computer Vision Engineer  
📍 Télécom Physique Strasbourg | VTEC Lasers & Sensors  
📫 mailto : oualid.allouch@etu.unistra.fr 
🌐 [LinkedIn](https://www.linkedin.com/in/oualid-allouch-608b3738a/) 


