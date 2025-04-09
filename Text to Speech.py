# This code is run only 1 time 


# import pyttsx3
# f=pyttsx3.init()
# voice=f.getProperty("voices")
# f.setProperty("voices",voice[1].id)
# a=str(input("Enter your name: "))
# f.say("Hello"+a)
# f.runAndWait()






# This code is run only more then  times
import pyttsx3
f = pyttsx3.init()
voices = f.getProperty("voices")
f.setProperty("voice", voices[1].id)  
while True:
    a = input("Enter something (type 'bye' to exit): ")
    if a.lower() == 'bye':
        f.say("Goodbye! ")
        f.runAndWait()
        break
    f.say("You said " + a)
    f.runAndWait()
