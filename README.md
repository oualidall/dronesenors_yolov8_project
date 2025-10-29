# 🛰️ DroneSensors YOLOv8 Project

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
drone_yolov8_project/
├── src/
│ ├── annotate.py # fonction d’inférence/annotation YOLOv8
│ ├── utils.py # ré-export utilitaire
│ └── init.py
├── scripts/
│ ├── extract_frames.py # extraction de frames depuis .mp4
│ └── annotate_batch.py # annotation en batch -> JSON
├── data/
│ └── samples/ # quelques images d’exemple (légères)
├── annotations/
│ └── examples/ # quelques JSON d’exemple
├── results/ # résultats, logs (vide par défaut)
├── Makefile # commandes pratiques
├── requirements.txt
└── README.md





> Les dossiers lourds (`data/`, `annotations/`, `results/`, `models/`) sont suivis via `.gitkeep`  
> et seuls de **petits échantillons** sont versionnés pour garder le repo léger.

---

## ⚙️ Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
