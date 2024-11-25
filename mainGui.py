import tkinter as tk
from tkinter import filedialog, messagebox
import pydub
import pygame
import os
import time  # Importation de time pour mesurer la durée
from Transcript import transcribe_audio
from Summerize import summerize

def convert_ogg_to_wav(ogg_file):
    audio = pydub.AudioSegment.from_ogg(ogg_file)
    wav_file = "converted_file.wav"
    audio.export(wav_file, format="wav")
    return wav_file

class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Transcription et Résumé Audio")

        # Initialisation de Pygame Mixer pour lire des fichiers audio
        pygame.mixer.init()
        self.is_playing = False  # Indicateur pour savoir si la musique joue
        self.is_paused = False   # Indicateur pour savoir si la musique est en pause
        self.current_file = None  # Fichier audio actuellement chargé
        # Configuration des frames
        self.create_frames()
        # Configuration des widgets dans chaque frame
        self.create_widgets()

    def create_frames(self):
        """Créer les frames pour la disposition gauche et droite"""
        # Frame pour la partie gauche
        self.left_frame = tk.Frame(self.root, padx=20, pady=20)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Frame pour la partie droite
        self.right_frame = tk.Frame(self.root, padx=20, pady=20)
        self.right_frame.pack(side=tk.LEFT, fill=tk.Y)

    def create_widgets(self):
        """Créer les widgets dans les frames gauche et droite"""

        # Part 1: Widgets pour la partie gauche
        self.open_button = tk.Button(self.left_frame, text="Ouvrir un fichier .ogg", command=self.open_file)
        self.open_button.pack(pady=10)

        # Zone pour afficher le chemin du fichier
        self.file_path_label = tk.Label(self.left_frame, text="Aucun fichier sélectionné", width=50)
        self.file_path_label.pack(pady=5)

        # Bouton pour jouer le fichier
        self.play_button = tk.Button(self.left_frame, text="Play", state=tk.DISABLED, command=self.toggle_play)
        self.play_button.pack(pady=5)

        # Zone de texte pour afficher la transcription (non éditable)
        self.transcription_label = tk.Label(self.left_frame, text="Transcription", font=("Arial", 12))
        self.transcription_label.pack(pady=5)
        self.transcription_text = tk.Text(self.left_frame, height=15, width=75, wrap=tk.WORD, state=tk.DISABLED)
        self.transcription_text.pack(pady=5)

        # Bouton pour effectuer la transcription
        self.transcribe_button = tk.Button(self.left_frame, text="Transcrire", state=tk.DISABLED, command=self.transcribe_audio)
        self.transcribe_button.pack(pady=10)

        # Label pour afficher le temps de transcription
        self.transcription_time_label = tk.Label(self.left_frame, text="Temps de transcription: 0.0s")
        self.transcription_time_label.pack(pady=5)

        # Part 2: Widgets pour la partie droite
        self.preprompt_label = tk.Label(self.right_frame, text="Préprompt pour résumé", font=("Arial", 12))
        self.preprompt_label.pack(pady=5)
        self.preprompt_text = tk.Text(self.right_frame, height=4, width=75, wrap=tk.WORD)
        self.preprompt_text.pack(pady=5)

        # Zone de texte pour afficher le résumé
        self.summary_label = tk.Label(self.right_frame, text="Résumé", font=("Arial", 12))
        self.summary_label.pack(pady=5)
        self.summary_text = tk.Text(self.right_frame, height=15, width=75, wrap=tk.WORD, state=tk.DISABLED)
        self.summary_text.pack(pady=5)

        # Bouton pour générer le résumé
        self.summarize_button = tk.Button(self.right_frame, text="Résumé", state=tk.DISABLED, command=self.summarize_text)
        self.summarize_button.pack(pady=10)

        # Label pour afficher le temps de résumé
        self.summary_time_label = tk.Label(self.right_frame, text="Temps de résumé: 0.0s")
        self.summary_time_label.pack(pady=5)

    def open_file(self):
        """Ouvre le fichier audio"""
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.ogg")])
        if file_path:
            self.file_path_label.config(text=file_path)
            self.audio_file_path = file_path
            self.current_file = file_path

            self.play_button.config(state=tk.NORMAL)
            self.transcribe_button.config(state=tk.NORMAL)

    def toggle_play(self):
        """Lancer/mettre en pause la lecture."""
        if self.is_playing:
            self.pause_audio()
        else:
            self.play_audio()

    def play_audio(self):
        """Jouer le fichier audio."""
        if self.current_file:
            pygame.mixer.music.load(convert_ogg_to_wav(self.current_file))  # Charger le fichier audio
            pygame.mixer.music.play()  # Démarrer la lecture
            self.is_playing = True
            self.play_button.config(text="Pause")  # Changer le texte du bouton à Pause

    def pause_audio(self):
        """Mettre en pause la lecture."""
        pygame.mixer.music.pause()  # Mettre en pause la musique
        self.is_paused = True
        self.is_playing = False
        self.play_button.config(text="Play")  # Changer le texte du bouton à Play

    def transcribe_audio(self):
        """Lance la transcription et mesure le temps"""
        start_time = time.time()  # Mesurer le temps de début de la transcription
        try:
            transcription = transcribe_audio(self.audio_file_path)
            self.transcription_text.config(state=tk.NORMAL)  # Rendre la zone éditable temporairement
            self.transcription_text.delete(1.0, tk.END)
            self.transcription_text.insert(tk.END, transcription)
            self.transcription_text.config(state=tk.DISABLED)  # Re rendre la zone non éditable

            # Mesurer et afficher le temps écoulé pour la transcription
            end_time = time.time()
            transcription_duration = round(end_time - start_time, 2)
            self.transcription_time_label.config(text=f"Temps de transcription: {transcription_duration}s")

            self.summarize_button.config(state=tk.NORMAL)  # Active le bouton Résumer
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la transcription : {e}")

    def summarize_text(self):
        """Génère le résumé et mesure le temps"""
        start_time = time.time()  # Mesurer le temps de début du résumé
        try:
            transcription = self.transcription_text.get(1.0, tk.END).strip()
            preprompt = self.preprompt_text.get(1.0, tk.END).strip()
            full_prompt = preprompt + "\n" + transcription
            summary = summerize(full_prompt)

            self.summary_text.config(state=tk.NORMAL)  # Rendre la zone éditable temporairement
            self.summary_text.delete(1.0, tk.END)
            self.summary_text.insert(tk.END, summary)
            self.summary_text.config(state=tk.DISABLED)  # Re rendre la zone non éditable

            # Mesurer et afficher le temps écoulé pour le résumé
            end_time = time.time()
            summary_duration = round(end_time - start_time, 2)
            self.summary_time_label.config(text=f"Temps de résumé: {summary_duration}s")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du résumé : {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    