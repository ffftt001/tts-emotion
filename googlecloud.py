from flask import Flask, request, jsonify, render_template
import azure.cognitiveservices.speech as speechsdk
import base64
from flask_cors import CORS
from google.cloud import language_v1
import os, re

app = Flask(__name__)
CORS(app)

# Google Cloud Natural Language API Setup
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"skilful-album-416720-e8ae8921e605.json" #change to your file path
google_client = language_v1.LanguageServiceClient()

@app.route('/')
def home():
    return render_template('frontend.html')

def analyze_emotion(text):
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = google_client.analyze_sentiment(document=document).document_sentiment
    return interpret_emotion(sentiment.score, sentiment.magnitude)

def interpret_emotion(score, magnitude):
    if score > 0.5:
        return 'cheerful' if magnitude > 0.5 else 'neutral'
    elif score < -0.25:
        return 'angry' if magnitude > 0.5 else 'sad'
    else:
        return 'neutral'

def map_emotion_to_style(emotion):
    emotion_to_style_map = {
        'cheerful': 'cheerful',
        'sad': 'sad',
        'angry': 'angry',
        'neutral': 'general'
    }
    return emotion_to_style_map.get(emotion, 'general')

def text_to_speech(subscription_key, service_region, text, language, voice_name, emotion):
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)
    speech_config.speech_synthesis_language = language
    speech_config.speech_synthesis_voice_name = voice_name
    
    # Determine the style based on emotion
    if emotion in ['cheerful', 'sad', 'angry', 'terrified']:
        style = emotion
    else:
        style = 'general'  # Fallback to a general style for neutral or undefined emotions

    # Use SSML to apply the style and make speech more natural
    ssml_text = f'''
    <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xml:lang="{language}">
        <voice name="{voice_name}">
            <mstts:express-as style="{style}">
                {text}
            </mstts:express-as>
        </voice>
    </speak>
    '''

    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    result = synthesizer.speak_ssml_async(ssml_text).get()
    
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        audio_data = result.audio_data
        audio_base64 = base64.b64encode(audio_data).decode('utf-8')
        return audio_base64
    else:
        return None

@app.route('/synthesize', methods=['POST'])
def synthesize():
    data = request.json
    tts_subscription_key = 'bc125dcc9afa408bb5f28f5f4882ca16'  #change to your key
    service_region = 'eastus'  #change to your region
    language = data['language']
    voice_name = data['voiceName']
    
    sentences = re.split(r'[.!?]+', data['text'])
    sentences = [sentence.strip() for sentence in sentences if sentence]
    audio_segments = []

    for sentence in sentences:
        emotion = analyze_emotion(sentence)
        audio_base64 = text_to_speech(tts_subscription_key, service_region, sentence, language, voice_name, emotion)
        if audio_base64:
            audio_segments.append(audio_base64)
    
    if audio_segments:
        return jsonify({'audioSegments': audio_segments})
    else:
        return jsonify({'error': 'Failed to synthesize speech for the segments'}), 500

if __name__ == '__main__':
    app.run(debug=True)
