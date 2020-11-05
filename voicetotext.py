import speech_recognition as sr

def p():
    r = sr.Recognizer()

    with sr.Microphone() as s:

        print("Speak...")
        r.pause_threshold = 0.6
        audio = r.listen(s)

        try:
            ask = r.recognize_google(audio, language = 'eng-us')
            with open('s.txt', 'w') as o:
                o.write(ask)
            print(f"You said : {ask}")
        except Exception:
            print("Didn't recognize...")
            return ""

        return ask

p()




