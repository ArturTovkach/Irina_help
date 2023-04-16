import random
import sys
import webbrowser


import speech_recognition as sr

import pyttsx3

import os


engine = pyttsx3.init()
name = 'Ирина'
engine.say(f'Привет, меня зовут {name} и я голосовой помощник. Чтобы ознакомиться со спектром команд скажите инфо')
engine.runAndWait()
while True:


    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)


    def HowAreYou():
        if text == 'Как дела':
            variants = ['Всё хорошо', 'Пойдет', 'Лучше не говорить', 'Плохо']
            choice = random.choice(variants)
            engine.say(f'{choice}')
            engine.runAndWait()
            exit()

    def WhatsYourName():
        if text == 'Ирина':
            engine.say(f'Да, могу ли я вам помочь?')


    def info():
        if text == 'инфо':
            engine.say('Я голосовой помощник созданный, чтобы облегчить пользование вашим устройством. На данный момент вам доступны такие команды: инфо, поиск, видео, котики, телеграм, погода. Чем я могу быть полезна?')
            engine.runAndWait()





    def weather():
        if text == 'Какая сейчас погода':
            get_weather()

    def get_weather():
        engine.say('Уточните, пожалуйста, ваш город?, я сейчас поддерживаю только письменный ввод города')
        engine.runAndWait()
        weath = input('Пропишите ваш город:')
        url = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0' + weath
        webbrowser.get().open(url)
        exit()

    def stop():
        if text == 'Ирина отбой':
            sys. exit()

    def google():
        if text == 'поиск':
            engine.say('Что вам найти, я могу обрабатывать только текст, поэтому введите, пожалуйста')
            engine.runAndWait()
            search = input('Введите ваш запрос: ')
            gu = 'https://www.google.com/search?q=' + search
            webbrowser.get().open(gu)
            exit()
    def kotiki():
        if text == 'котики':
            engine.say('Вот вам немного милоты <3')
            engine.runAndWait()
            webbrowser.get().open('https://www.pinterest.com/search/pins/?q=%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B8&rs=typed')
            exit()

    def youtube():
        if text == ("видео"):
            engine.say('Введите ваш запрос, пожалуйста, в терминал')
            engine.runAndWait()
            youtube = input('Ваш запрос: ')
            webbrowser.get().open('https://www.youtube.com/results?search_query=' + youtube)
            exit()

    def telegram():
        if text == 'Telegram':
            engine.say('Открываю приложение Telegram')
            engine.runAndWait()
            os.startfile(r'C:\Users\admin\AppData\Roaming\Telegram Desktop\Telegram.exe')
            exit()

    def exit():
        engine.say('Могу ли я вам ещё чем-то помочь?Если нет, то скажите стоп')
        engine.runAndWait()


    try:

        text = r.recognize_google(audio, language='ru-RU')
        print(f"Вы сказали: {text}")
        HowAreYou()
        info()
        stop()
        weather()
        google()
        kotiki()
        youtube()
        telegram()
        exit()

    except sr.UnknownValueError:
        engine.say("Я не смогла распознать речь. Повторите ваш запрос")
        engine.runAndWait()
    except sr.RequestError as e:
        print(f"Произошла ошибка {e}")
    except sr.WaitTimeoutError:
        print("Can you check if your microphone is on, please?")




