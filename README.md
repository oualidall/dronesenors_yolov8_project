# 🛰️ DroneSensors YOLOv8 Project

<p align="center">
  <img src="docs/pipeline_overview.png" alt="YOLOv8 Drone Pipeline" width="700"/>
</p>

<p align="center">
  <img src="docs/pipeline_overview.png" alt="YOLOv8 Drone Pipeline" width="700"/>
</p>


**Auteur :** Oualid Allouch  
**Entreprise :** VTEC Lasers & Sensors Ltd. (Eindhoven, NL)  
**Rôle :** AI & Computer Vision Intern — Juin–Août 2025  

---

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


