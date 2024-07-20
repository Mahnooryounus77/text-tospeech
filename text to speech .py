import pyttsx3
project = pyttsx3.init()
speech =input("enter the text: ")
project.say(speech)
        
project.runAndWait()


