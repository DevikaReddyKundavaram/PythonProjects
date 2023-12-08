import win32com.client
import speech_recognition as sr
import webbrowser
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold= 1
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language="en-in")
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "Some Error occured.Sorry from JARVIS"
speaker = win32com.client.Dispatch("SAPI.SpVoice")
while 1:
    #print("Enter the word you want to speak it out by computer")
    speaker.Speak("Hello Nikki Speak Something")
    print("Listening...")
    text=takeCommand()
    speaker.Speak(text)
    '''l=["Open Youtube".lower(),"Open google".lower()]
    S=["https://youtube.com","https://google.com"]
    i=0
    while 1:
         if l[i]==text:
            speaker.speak("Opening ....")
            webbrowser.open(S[i])
         i+=1'''

