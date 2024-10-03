# pip install pyaudio
# pip install flask flask-cors eventlet SpeechRecognition

from flask import Flask, jsonify, request
from flask_cors import CORS
import speech_recognition as sr
import threading
import queue
import os

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

recognizer = sr.Recognizer()
microphone = sr.Microphone()
audio_queue = queue.Queue()
is_recording = False
output_file = "realtime_speech_output.txt"

def listen_in_background():
    global is_recording
    while is_recording:
        try:
            with microphone as source:
                audio = recognizer.listen(source, phrase_time_limit=3)
                audio_queue.put(audio)
        except sr.WaitTimeoutError:
            pass

def process_audio():
    global is_recording
    while is_recording:
        try:
            audio = audio_queue.get(timeout=0.5)
            try:
                text = recognizer.recognize_google(audio, show_all=False)
                print(f"Recognized: {text}")
                with open(output_file, "a") as file:
                    file.write(text + " ")
            except sr.UnknownValueError:
                print("Could not understand the audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
        except queue.Empty:
            pass

@app.route('/start', methods=['POST'])
def start_recording():
    global is_recording
    if not is_recording:
        is_recording = True
        open(output_file, 'w').close()  # Clear the file
        threading.Thread(target=listen_in_background, daemon=True).start()
        threading.Thread(target=process_audio, daemon=True).start()
        return jsonify({"status": "Recording started"}), 200
    return jsonify({"status": "Already recording"}), 400

@app.route('/stop', methods=['POST'])
def stop_recording():
    global is_recording
    if is_recording:
        is_recording = False
        return jsonify({"status": "Recording stopped"}), 200
    return jsonify({"status": "Not recording"}), 400

@app.route('/text', methods=['GET'])
def get_text():
    if os.path.exists(output_file):
        with open(output_file, 'r') as file:
            content = file.read()
        return jsonify({"text": content}), 200
    return jsonify({"text": ""}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
