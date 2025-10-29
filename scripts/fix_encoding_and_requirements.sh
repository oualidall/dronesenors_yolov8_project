#!/usr/bin/env bash
set -euo pipefail

echo "[*] Scan des .py non UTF-8…"
BAD_FILES=$(find . -type f -name "*.py" -exec file -i {} \; | awk -F: '$2 !~ /utf-8/ {print $1}')
if [ -z "$BAD_FILES" ]; then
  echo "[*] OK: tous les .py sont en UTF-8."
else
  echo "[!] Fichiers non UTF-8 détectés :"
  echo "$BAD_FILES"
  for f in $BAD_FILES; do
    # Détection du charset
    CS=$(file -i "$f" | sed -E 's/.*charset=([^ ]+).*/\1/')
    echo "    -> Convertir $f (charset=$CS) -> UTF-8"
    case "$CS" in
      iso-8859-1|us-ascii|windows-1252|latin1)
        iconv -f "$CS" -t UTF-8 "$f" -o "$f.tmp" && mv "$f.tmp" "$f"
        ;;
      *)
        # tentative générique : s'il échoue, on essaie windows-1252
        if ! iconv -f "$CS" -t UTF-8 "$f" -o "$f.tmp" 2>/dev/null; then
          iconv -f windows-1252 -t UTF-8 "$f" -o "$f.tmp" || { echo "    [x] Échec conversion $f"; exit 1; }
          mv "$f.tmp" "$f"
        else
          mv "$f.tmp" "$f"
        fi
        ;;
    esac
    # Ajoute un header d'encodage Python si absent (utile sous Py3.12-)
    head -n1 "$f" | grep -qi "coding" || sed -i '1i# -*- coding: utf-8 -*-' "$f"
  done
fi

echo "[*] (Re)génère requirements.txt avec pipreqs…"
rm -f requirements.txt
pipreqs --encoding utf-8 --force .

# s'assurer que ultralytics est bien listé
grep -q "^ultralytics" requirements.txt || echo "ultralytics>=8.3.0" >> requirements.txt

echo "[✓] requirements.txt prêt."
