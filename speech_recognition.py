import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as mic:
    print('you can start talking now')
    audio = rec.listen(mic)
    print('Time is over')
    print('Text:' + rec.recognize_google(audio))
