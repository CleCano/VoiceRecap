#!/bin/bash

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null
then
    echo "Python3 n'est pas installé. Veuillez installer Python3."
    exit
else
    echo "Python3 est installé."
fi

# Vérifier si pip est installé
if ! command -v pip3 &> /dev/null
then
    echo "pip3 n'est pas installé. Installation de pip3..."
    sudo apt-get install python3-pip -y
else
    echo "pip3 est installé."
fi

# Installer les dépendances Python
echo "Installation des dépendances Python..."
pip3 install openai google-cloud-speech pydub pygame

# Vérifier si tkinter est installé
if ! python3 -c "import tkinter" &> /dev/null
then
    echo "tkinter n'est pas installé. Installation de tkinter..."
    sudo apt-get install python3-tk -y
else
    echo "tkinter est installé."    
fi

echo "Toutes les dépendances sont installées."