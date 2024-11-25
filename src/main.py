import io
import argparse
import Transcript
import Summerize
if __name__ == "__main__":
    # Configurer l'analyse des arguments
    parser = argparse.ArgumentParser(description="Transcrire un fichier audio .ogg avec Google Cloud Speech-to-Text")
    parser.add_argument("file_path", help="Chemin du fichier audio (.ogg)")
    args = parser.parse_args()

    # Passer le chemin du fichier à la fonction
    transcript = Transcript.transcribe_audio(args.file_path)
    summerize = Summerize.summerize("Fais un résumé de cette transcription de message vocal" + str(transcript))
    print(f"Transcription : {transcript}")
    print(f"Résumé : {summerize}")