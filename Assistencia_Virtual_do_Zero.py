#bibliotecas

from gtts import gTTS
import speech_recognition as sr
import os
from datetime import datetime
import playsound
import pyjokes
import pyaudio
import webbrowser
import winshell
from pygame import mixer


#capturar audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language='pt-BR')
            print(said)
        except sr.UnknownValueError:
            speak("Desculpe, não entendi.")
        except sr.RequestError:
            speak("Desculpe, o serviço não está disponível")
    return said.lower()

#converter texto em audio
def speak(text):
    tts = gTTS(text=text, lang='pt-br')
    filename = "voice.mp3"
    mixer.quit()
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    while mixer.music.get_busy():
        pass

#funcções para respostas do comando de áudio
def respond(text):
    print("texto através do áudio " + text)
    if 'youtube' in text:
        speak("O que você quer pesquisar?")
        keyword = get_audio()
        if keyword!= '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Aqui está o que encontrei para {keyword} no YouTube")
    elif 'hora' in text:
        strTime = datetime.today().strftime("%H:%M %p")
        print(strTime)
        speak(strTime)
    elif 'sair' in text:
        speak("Goodbye, até a próxima.")
        exit()


while True:
    print("estou ouvindo...")
    text = get_audio()
    respond(text)