
# VoiceRecap

VoiceRecap is a tool that transcribes audio files (.ogg format) and summarizes the transcriptions using Google Cloud Speech-to-Text and OpenAI's GPT-4o-mini model.
## Important 

1. This project is configured to work with .ogg files only. If you want to use other audio formats, you can convert them to .ogg.

2. The project works in French for now. But I will add more languages in the future.
## Prerequisites

- Python 3.x
- Google Cloud account with Speech-to-Text API enabled
- OpenAI API key

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/voicerecap.git
    cd voicerecap
    ```

2. Run the installation script to install the necessary dependencies:

    ```sh
    ./install.sh
    ```
3. If the script fails to install the dependencies, you can install them manually using the following commands:

### Manual Installation
Install Python3
```sh
    sudo apt-get install python3
```
Install pip3
```sh
    sudo apt-get install python3-pip
```
Install the required Python packages:
```sh
    pip3 install openai google-cloud-speech pydub pygame
```

## Google Cloud Setup

1. Create a Google Cloud project and enable the Speech-to-Text API.

2. Create a service account and download the JSON key file.

3. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your JSON key file:

    ```sh
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/JSONKEYFILE.json"
    ```
## OpenAI Setup

1. Create an account on [OpenAI](https://www.openai.com/).

2. Generate an API key from the OpenAI dashboard.

3. Set the `OPENAI_API_KEY` environment variable to your API key:

    ```sh
    export OPENAI_API_KEY="your_openai_api_key"
    ```

## Usage

### Command Line Interface

To transcribe an audio file and summarize the transcription, use the following command:

```sh
launch.sh path/to/your/audiofile.ogg
```



### Graphical User Interface

1. Run the GUI application:

    ```sh
    ./launch.sh -G
    ```

2. Use the GUI to open an `.ogg` audio file, play it, transcribe it, and generate a summary.

