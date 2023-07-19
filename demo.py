import argostranslate.translate
import argostranslate.package
from vosk import Model, KaldiRecognizer
import pyaudio


model = Model(r"/home/aaryan/Downloads/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

from_code = "en"
to_code = "es"

mic = pyaudio.PyAudio()
print("say something")
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)

    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(f"' {text[14:-3]} '")
        speech_text = text[14:-3]  # Extract the recognized speech from the result
        translatedText = argostranslate.translate.translate(speech_text, from_code, to_code)
        print(f"Speech: {speech_text}")
        print(f"Translation: {translatedText}")