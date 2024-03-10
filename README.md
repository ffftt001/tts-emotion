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

### Get related API and service
- Obtaining Azure Speech Service API Key and Service Region
  1. Sign in to Azure Portal
      - Visit the Azure Portal and sign in using your Azure account credentials.

  2. Create Speech Service Resource
      - Navigate to the Azure portal dashboard and click on the "+" button to create a new resource.

  3. Search for Speech Service
      - In the search bar, type "Speech" and select Speech from the results.

  4. Configure Speech Service
      - Choose a subscription.
      - Create a new resource group or select an existing one.
      - Enter a name for the Speech service.
      - Choose the region closest to your location for better performance.
      - Select the pricing tier according to your requirements.
  5. Obtain API Key and Service Region
      - Once the Speech service is created, navigate to the Keys and Endpoint section of the newly created Speech service resource. Here, you will find the API key and the service region.

- Obtaining Google Cloud Natural Language API Credentials
  1. Sign in to Google Cloud Console
      - Visit the Google Cloud Console and sign in using your Google account credentials.

  2. Create or Select a Project
      - Create a new project or select an existing one where you want to use the Natural Language API.

  3. Enable the Natural Language API
      - Navigate to the APIs & Services > Library section in the left sidebar. Search for "Natural Language API" and enable it for your project.

  4. Create Service Account and Generate JSON Key
      - Navigate to the APIs & Services > Credentials section.
      - Click on Create credentials and select Service account key.
      - Choose or create a service account, select the role (e.g., Project > Owner) and key type (JSON).
      - Click Create to generate and download the JSON key file.
  5. Store the JSON Key Securely
      - Store the downloaded JSON key file securely in your project directory. Avoid committing it to version control systems for security reasons.

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
