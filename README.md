# tts-with-emotion

### SUMMARY

A common problem with AI voiceovers involves its lack of realism, especially in the aspects of emotion and tone. This project attempts to improve the functionality of text-to-speech (TTS) of AI voices through finetuning existing TTS models to better incorporate human emotion, creating a more realistic and immersive AI audio experience. 


### This project is mainly built With

- [Flask](https://github.com/pallets/flask)
- [Azure Cognitive Services Speech SDK](https://github.com/Azure-Samples/cognitive-services-speech-sdk)
- [Flask-CORS](https://github.com/corydolphin/flask-cors)
- [Google Cloud Language API](https://cloud.google.com/natural-language/docs/basics)


### FILE FORMAT

The file consists of frontend.html, which is the user interface for the TTS model. By inputting text, an AI generated speech is output, incorporating human emotion into its speech. googlecloud.py is the backend coding that supports the process of adding emotion to speech.

### Get Google cloud service and Azure Cognitive Services key, and the .json file

### SETUP

1. Make sure Python 3.6+ is installed.
2. clone this respository and change the directory.
```
git clone https://github.com/ffftt001/tts-emotion.git
cd tts-emotion
```
3. Install all the library required.
```
pip install -r requirement.txt
```

4. Update *`GOOGLE_APPLICATION_CREDENTIALS`* to the path of your Google Cloud service account key file.
Update *`Azure Cognitive Services keys`* and *`region`* in the `"googlecloud.py"` file.


5. Run `"googlecloud.py"` file.
```
python googlecloud.py
```
6. Run the html file in a new cmd prompt/ terminal.
```
cd tts-emotion
```
  - if using window:
    ```
    start frontend.html
    ```
  - if using mac/linux:
    ```
    open frontend.html
    ```
