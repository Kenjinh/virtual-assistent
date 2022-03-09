from datetime import datetime
import pywhatkit as kit
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('voice', 'brazil')
audio = sr.Recognizer()

engine.say('Qual mensagem deseja enviar?')
engine.runAndWait()
with sr.Microphone() as source:
    voice = audio.listen(source)
    mic = audio.recognize_google(voice, language='pt-BR')
    mic = str(mic.lower())
    print(mic)
    try:
        data = datetime.now().strftime('%H:%M:%S')
        hora = int(data[0:2])
        minuto = int(data[3:5]) + 1
        segundo = int(data[6:8])
        kit.sendwhatmsg('+5511972892900', mic, hora, minuto, segundo)
        engine.say('Mensagem enviada para amor')
        engine.runAndWait() 
    except Exception as e:
        print(e)