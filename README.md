# tts-emotion

### SUMMARY

A common problem with AI voiceovers involves its lack of realism, especially in the aspects of emotion and tone. This project attempts to improve the functionality of text-to-speech (TTS) of AI voices through finetuning existing TTS models to better incorporate human emotion, creating a more realistic and immersive AI audio experience. 


### PREREQUISITES

Refer to requirement.txt for the full list of prerequisites needed to run the project.


### FILE FORMAT

The file consists of frontend.html, which is the user interface for the TTS model. By inputting text, an AI generated speech is output, incorporating human emotion into its speech. googlecloud.py is the backend coding that supports the process of adding emotion to speech.


### SETUP

1. Make sure Python 3.6+ is installed.
2. Set up a Virtual Environment.
  >$python -m venv tts-env

  >source tts-env/bin/activate
3. Install Flask and other dependencies.
  >pip install Flask azure-cognitiveservices-speech google-cloud-languages
4. Set GOOGLE_APPLICATION_CREDENTIALS to the path of your Google Cloud service account key file.
Set Azure Cognitive Services keys and region in your application.
5. Run the Flask Application.
  >flask run


### DATASET and AI MODEL

The dataset used can be generated by running the code as in:



>$git clone https://github.com/ffftt001/tts-emotion.git

>$cd tts-emotion

>$pip install -r requirement.txt

>$python googlecloud.py

>$python -m http.server

>$cd tts-emotion
>$python -m http.server &
open http://localhost:8000/frontend.html








