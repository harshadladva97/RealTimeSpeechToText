# RealTimeSpeechToText

This repository contains a Real-Time Speech-to-Text application built with Next.js for the frontend and Python Flask for the backend. The system captures audio input from the user and transcribes it into text in real-time using speech recognition technologies.

## Note:

The installation steps are only allowed in ubuntu machine.

## Installation (Run Backend):

1. Clone the application.

```bash
git clone https://github.com/harshadladva97/RealTimeSpeechToText.git
cd RealTimeSpeechToText
```

2. Install flask in the python.

```bash
For ubuntu:

pip install virtualenv
virtualenv venv
source ./venv/bin/activate
pip install flask flask-cors eventlet SpeechRecognition pyaudio # Install all the required packages.
```

3. Run the backend using following command:

```bash
python3 app.py
```

## Installation (Run Frontend):

1. Go to the `frontend` folder in the application.

```bash
cd frontend`
```

2. Install npm packages.

```bash
pnpm install
```

3. Run the frontend application.

```bash
pnpm run dev
```

4. Open the browser with `http://127.0.0.1:3000`.

## Use cases:

1. The application use the microphone to record the speech and transcribing the recording into the text.
2. It will transcribing text in realtime. (Note: If you don't catch the text then please check your microphone, background noise and your words should be very clear for understanding)

## How to use:

1. Press on "Start Recording" Button.

2. Once it will start recoding, please start speaking in microphone.

3. To stop the recording. Please press on the "Stop Recording" button.
