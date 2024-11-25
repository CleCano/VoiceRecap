from google.cloud import speech
import io
import threading
import itertools
import time
import sys
def spinner_animation(message="Transcription en cours..."):
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    while not stop_spinner.is_set():
        sys.stdout.write(f"\r{message} {next(spinner)}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * len(message) + "\r")  # Effacer la ligne


def transcribe_audio(file_path):

    
    # Démarrer le spinner dans un thread séparé
    global stop_spinner
    stop_spinner = threading.Event()
    spinner_thread = threading.Thread(target=spinner_animation)
    spinner_thread.start()

    try:
        # Initialiser le client
        client = speech.SpeechClient()

        # Charger le fichier audio
        with io.open(file_path, "rb") as audio_file:
            content = audio_file.read()

        # Configurer le fichier audio
        audio = speech.RecognitionAudio(content=content)
        
        # Spécifier le type de configuration pour la reconnaissance
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.OGG_OPUS,
            sample_rate_hertz=16000,  # Vérifiez le taux d'échantillonnage exact de votre fichier .ogg
            language_code="fr-FR"  # Changez "fr-FR" selon votre langue
        )

        # Envoyer la requête pour la reconnaissance vocale
        response = client.recognize(config=config, audio=audio)

        # Arrêter le spinner
        stop_spinner.set()
        spinner_thread.join()
        resultText = ""
        # Extraire la transcription
        if not response.results:
            print("\nAucune transcription n'a été trouvée.")
        else:
            for result in response.results:
                resultText += str(result.alternatives[0].transcript)

    except Exception as e:
        stop_spinner.set()
        spinner_thread.join()
        print(f"\nErreur : {e}")

    print("Transcription terminée.")
    return resultText