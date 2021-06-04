import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib



engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
# print(voices[0].id)
# print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am gangan   ")

def takeCommand():
    ''' takes audio from user and returns string output '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1

        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(f"Say that again please {e} ")
        return "None"
    return query

def sendEmail(to,content):
    #smtp
    #have to enable less secure apps in gmail , google it
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com","yourpassword")
    #instead of writing password here , save pass in txt file and retrieve string from it
    server.sendmail("yourmail@gmail.com",to,content)
    server.close()




if __name__ == '__main__':
    wishMe()
    while True:
        if 1:


            query=takeCommand().lower()
            #logic for executing tasks based on query
            if 'wikipedia' in query :
                speak('Searching wikipedia')
                query=query.replace("wikipedia"," ")
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in query:
                speak("Opening Youtube ")
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
            elif 'music' in query :
                music_directory="E:\\Metallica - Metallica (1991) (PBTHAL LP 24-96) [FLAC] vtwin88cube"
                songs=os.listdir(music_directory)
                print(songs)
                random_song=random.randint(0,len(songs)-1)
                os.startfile(os.path.join(music_directory,songs[random_song]))
                speak(f"Playing {songs[random_song]} ")
            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")
            elif 'open code' in query :
                pycharm="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
                # chrome="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(pycharm)
            elif 'email to harry' in query :
                try:
                    speak("What should i say")
                    content=takeCommand()
                    to ="kjshdfkj@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak(f"Sorry can not send")
            elif 'favourite food' in query :
                speak("Although it depends on the mood , but I like eedli Sambar the most ")
            elif 'favourite colour' in query :
                speak("Well...,I prefer Maroon ")
            elif 'iphone' in query :
                os.system('cmd /c "netsh wlan show networks "')
                name_of_router = "Broadband21"
                speak(os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"'''))

                # import module
                import os


                # function to establish a new connection
                def createNewConnection(name, SSID, password):
                    config = """<?xml version=\"1.0\"?>
                <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
                    <name>""" + name + """</name>
                    <SSIDConfig>
                        <SSID>
                            <name>""" + SSID + """</name>
                        </SSID>
                    </SSIDConfig>
                    <connectionType>ESS</connectionType>
                    <connectionMode>auto</connectionMode>
                    <MSM>
                        <security>
                            <authEncryption>
                                <authentication>WPA2PSK</authentication>
                                <encryption>AES</encryption>
                                <useOneX>false</useOneX>
                            </authEncryption>
                            <sharedKey>
                                <keyType>passPhrase</keyType>
                                <protected>false</protected>
                                <keyMaterial>""" + password + """</keyMaterial>
                            </sharedKey>
                        </security>
                    </MSM>
                </WLANProfile>"""
                    command = "netsh wlan add profile filename=\"" + name + ".xml\"" + " interface=Wi-Fi"
                    with open(name + ".xml", 'w') as file:
                        file.write(config)
                    os.system(command)


                # function to connect to a network
                def connect(name, SSID):
                    command = "netsh wlan connect name=\"" + name + "\" ssid=\"" + SSID + "\" interface=Wi-Fi"
                    os.system(command)


                # function to display avavilabe Wifi networks
                def displayAvailableNetworks():
                    command = "netsh wlan show networks interface=Wi-Fi"
                    os.system(command)


                # display available netwroks
                displayAvailableNetworks()

                # input wifi name and password
                name = input("Name of Wi-Fi: ")
                password = input("Password: ")

                # establish new connection
                createNewConnection(name, name, password)

                # connect to the wifi network
                connect(name, name)
                print("If you aren't connected to this network, try connecting with the correct password!")

