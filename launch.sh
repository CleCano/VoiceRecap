#!/bin/bash

# Vérifier si l'option -G est présente
if [[ "$1" == "-G" ]]; then
    # Lancer mainGui.py
    python3 src/mainGui.py
else
    # Lancer main.py avec les arguments fournis
    python3 src/main.py "$@"
fi