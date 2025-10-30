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

## 🖼️ Exemple d’annotation (réel)

<p align="center">
  <img src="docs/example_annotation.jpg" alt="Exemple d’annotation YOLOv8 (réel)" width="700"/>
</p>

<p align="center">
  <em>Image <code>video2.mp4_frame0156.jpg</code> annotée automatiquement à partir du JSON généré par le pipeline YOLOv8.</em>
</p>

---

## 📄 Exemple d’annotation JSON

```json
{
  "image_filename": "video2.mp4_frame0156.jpg",
  "image_dimensions": { "width": 848, "height": 480 },
  "objects": [
    {
      "contour": { "x": 692.7708129882812, "y": 300.0146484375, "w": 53.48663330078125, "h": 32.495635986328125 },
      "obj_name": "car",
      "name_accuracy": 0.7056053876876831
    },
    {
      "contour": { "x": 559.8329467773438, "y": 281.91314697265625, "w": 40.7244873046875, "h": 19.373443603515625 },
      "obj_name": "car",
      "name_accuracy": 0.6810169816017151
    },
    {
      "contour": { "x": 718.6027221679688, "y": 275.9717712402344, "w": 28.551513671875, "h": 14.717376708984375 },
      "obj_name": "car",
      "name_accuracy": 0.4981396496295929
    },
    {
      "contour": { "x": 381.3439636230469, "y": 277.3162841796875, "w": 9.7493896484375, "h": 21.295318603515625 },
      "obj_name": "person",
      "name_accuracy": 0.357573002576828
    }
  ]
}


## 🔗 Contact

👨‍💻 **Oualid Allouch**  
AI & Computer Vision Engineer  
📍 Télécom Physique Strasbourg | VTEC Lasers & Sensors  
📫 mailto : oualid.allouch@etu.unistra.fr 
🌐 [LinkedIn](https://www.linkedin.com/in/oualid-allouch-608b3738a/) 


