"""Utilitaires du projet Drone YOLOv8.

Ce module ré-exporte la fonction d'annotation pour compatibilité
(backward-compat) si d'autres scripts importent encore `src.utils`.
"""
from .annotate import annotate_rgb_image

__all__ = ["annotate_rgb_image"]
