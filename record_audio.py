import speech_recognition as sr

def record_audio(filename="audio.wav"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Gravando... Fale algo.")
        audio = recognizer.listen(source)

    with open(filename, "wb") as file:
        file.write(audio.get_wav_data())
    print(f"Áudio gravado e salvo como {filename}.")
    return filename

audio_file = record_audio()

