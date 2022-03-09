from datetime import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit as kit

#Get engine pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'brazil')
audio = sr.Recognizer()

def get_command():
    try:
        with sr.Microphone() as source:
            print('Say something!')
            voice = audio.listen(source)
            command = audio.recognize_google(voice, language='pt-BR')
            command = command.lower()
            print(command)
            if 'verônica' in command:
                command = command.replace('verônica', '')
                print(command)


    except Exception as e:
        print (e)
    return command

def send_mensage(number):
    engine.say('Qual mensagem deseja enviar?')
    engine.runAndWait()
    with sr.Microphone() as source:
        print('Say something!')
        voice = audio.listen(source)
        mic = audio.recognize_google(voice, language='pt-BR')
        mic = str(mic.lower())
        try:
            data = datetime.now().strftime('%H:%M:%S')
            hour = int(data[0:2])
            minute = int(data[3:5]) + 1
            second = int(data[6:8])
            kit.sendwhatmsg(number, mic, hour, minute, second)
            engine.say('Mensagem enviada')
            engine.runAndWait() 
        except Exception as e:
            print(e)
                  
                
                

def commands():
    command = get_command()
    if 'dia é hoje' in command:
        engine.say(datetime.now().strftime('%d/%m/%Y'))
        engine.runAndWait()
    elif 'horas são' in command:
        engine.say(datetime.now().strftime('%H:%M'))
        engine.runAndWait()
    elif 'enviar mensagem' in command:
        engine.say('Para quem deseja enviar a mensagem ?')
        engine.runAndWait()
        with sr.Microphone() as source:
            print('Say something!')
            voice = audio.listen(source)
            mic = audio.recognize_google(voice, language='pt-BR')
            mic = mic.lower()
            if '' in mic: #insert person name
                send_mensage('') #insert phone number
            elif '' in mic: #insert person name
                send_mensage('') #insert phone number
            else:
                engine.say('Contato não encontrado')
                engine.runAndWait()
    elif 'pesquisar no youtube' or 'pesquisar youtube' in command:
        engine.say('Qual o nome do vídeo?')
        engine.runAndWait()
        if 'pesquisar no youtube' in command:
            command = command.replace('pesquisar no youtube', '')
        elif 'pesquisar youtube' in command:
            command = command.replace('pesquisar youtube', '')
        try:
            kit.playonyt(command)
        except Exception as e:
            print(e)

    else:
        engine.say('Não tenho esse comando')
        engine.runAndWait()


get_command()
commands()