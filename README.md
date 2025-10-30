![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-4.12.0-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

# 🛰️ DroneSensors YOLOv8 Project

**Auteur :** Oualid Allouch  
**Entreprise :** VTEC Lasers & Sensors Ltd. (Eindhoven, NL)  
**Rôle :** AI & Computer Vision Intern — Juin–Août 2025  

---

## 🧠 Pipeline global

<p align="center">
  <img src="docs/pipeline_overview.png" alt="YOLOv8 Drone Pipeline" width="700"/>
</p>

---

## 🎯 Objectif

Pipeline IA de bout en bout pour l’analyse de **vidéos de drones** en **surveillance environnementale** :

- Extraction automatique de frames depuis des vidéos,  
- Détection & annotation avec **YOLOv8** (Ultralytics),  
- Export des résultats au format **JSON** (prêt pour l’entraînement ou l’évaluation).

---

## 📦 Structure


drone_yolov8_project/
├── src/
│   ├── annotate.py          # Inference / annotation YOLOv8
│   ├── utils.py             # Fonctions utilitaires
│   └── __init__.py
│
├── scripts/
│   ├── extract_frames.py    # Extraction des frames depuis .mp4
│   ├── annotate_batch.py    # Annotation en batch -> JSON
│   └── visualize_json.py    # Visualisation des annotations
│
├── data/                    # Datasets (échantillons légers)
├── annotations/             # JSONs générés
├── results/                 # Logs & résultats
├── docs/                    # Documentation et exemples visuels
│   ├── pipeline_overview.png
│   ├── original_frame.jpg
│   ├── example_annotation.jpg
│   └── video2.mp4_frame0156.json
│
├── Makefile
├── requirements.txt
└── README.md

##🖼️ Exemple d’annotation YOLOv8
|                            Image originale                            |                              Image annotée                              |
| :-------------------------------------------------------------------: | :---------------------------------------------------------------------: |
| <img src="docs/original_frame.jpg" alt="Frame originale" width="400"> | <img src="docs/example_annotation.jpg" alt="Frame annotée" width="400"> |

