import datetime
import os
import requests
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import wolframalpha
import pyjokes
import pyautogui
from PIL import Image
import normalChat
from threading import Thread
from googletrans import Translator, LANGUAGES
import webScrapping
import cv2
import ToDo
import appControl
import dictionary
import math_function



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voice_id = 0  # 0 for female, 1 for male
ass_volume = 1  # max volume
ass_voiceRate = 200
ownerDesignation = "sir"
Name="kashish"


def speak(audio) -> object:
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("Good evening")
    print("hi, my name is taara, and how may i help you  ")
    speak("hye, my name is taara, and how may i help you  ")
    print("Enter your Name to start")
    speak("Enter your Name to start")
    global Name
    Name = input()
    speak("enter your Gender")
    print("enter your Gender( F,f=FEMALE , M,m=MALE) ")
    Gender = input()
    print("Name =" + Name)
    print("Gender =" + Gender)
    global ownerDesignation
    if Gender == "m":
        ownerDesignation = "Sir"
    else:
        ownerDesignation = "Maam"

def isContain(txt, lst):
	for word in lst:
		if word in txt:
			return True
	return False

def takecommand():
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    r.energy_threshold = 300
    r.pause_threshold = 0.6
    r.non_speaking_duration = 0.5
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        #
        audio = r.listen(source)

    try:
        print("recogninzing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)

        print("say that again please.....")
        return "None"
    return query


def clickPhoto():
    global imageName
    if os.path.exists('Camera') == False:
        os.mkdir('Camera')

    from time import sleep
    import playsound
    from datetime import datetime

    cam = cv2.VideoCapture(0)
    _, frame = cam.read()
    # playsound.playsound('extrafiles/audios/photoclick.mp3')
    imageName = 'Camera/Camera_' + str(datetime.now())[:19].replace(':', '_') + '.png'
    cv2.imwrite(imageName, frame)
    cam.release()
    cv2.destroyAllWindows()


def viewPhoto():
    from PIL import Image
    img = Image.open(imageName)
    img.show()

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def clickPhoto():
    global imageName
    if os.path.exists('Camera') == False:
        os.mkdir('Camera')

    from datetime import datetime
    import playsound

    cam = cv2.VideoCapture(0)
    _, frame = cam.read()
    playsound.playsound('extrafiles/audios/photoclick.mp3')
    imageName = 'Camera/Camera_' + str(datetime.now())[:19].replace(':', '_') + '.png'
    cv2.imwrite(imageName, frame)
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    #wishme()
    while True:
        query = takecommand().lower() # logic on based on task query

        if 'wikipedia' in query:
            speak("serching wikipedia.......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            print(results)
            speak("Accoding To wikipedia")
            speak(results)
        elif 'open youtube' in query:
            try:
                webbrowser.open("youtube.com")
                break
            except:
                print("say that again")
        elif 'open chrome' in query:
            webbrowser.open("google.com")


        # elif "hello" in query:
        # speak("hello , how are you")

        elif "fine" in query or "very nice" in query:
            speak("Great , so How can i help you")

        elif 'the time' in query or "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f", the time is {strtime}")

        elif 'open code' in query or "open source code " in query:
            codePath = "C:\\Users\\E:\Minor Project\Tarra"


        elif " Day " in query:
            tellDay()
            continue
        elif 'play music' in query:
            music_dir = "C:\\Users\\kashi\\Music\\"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            print("I was built by kashish Narang & Priyanka Prajapati")
            speak("I was built by kashish Narang and Priyanka Prajapati")

        elif "open stack overflow" in query:
            webbrowser.open_new_tab("https://stackoverflow.com/")
            speak("Here is stackoverflow")



        # elif 'who are you' in query or 'what can you do' in query:
        # speak('I am Tarra version 1 point O your personal assistant. I am programmed to minor tasks like'
        #      'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
        #    'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "temperature" in query:
            speak("whats the city name")
            location = takecommand()
            if location != "None":
                try:
                    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + "02c4be5475cd1da1275c305e6778a272"
                    api_link = requests.get(complete_api_link)
                    api_data = api_link.json()
                    current_temperature = int((api_data['main']["temp"]) - 273.15)
                    print(" The current temprature in " + location + " is " + format(
                        current_temperature) + " Degree Celsius")
                    speak(" The current temprature in " + location + "is" + format(
                        current_temperature) + "Degree Celsius")
                    print(complete_api_link)
                except:
                    print("sorry")
            else:
                print("please say clearly")


        elif "weather" in query:
            speak("whats the city name")
            location = takecommand()
            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + "02c4be5475cd1da1275c305e6778a272"
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()
            current_temperature = int((api_data['main']["temp"]) - 273.15)
            weather_desc = api_data['weather'][0]['description']
            print(" Right now in " + location + " its " + format(current_temperature) + " Degrees , " + weather_desc)
            speak(" Right now in " + location + " its " + format(current_temperature) + " Degrees and " + weather_desc)
            print(complete_api_link)





        elif 'hye' in query or 'hi' in query or 'hay' in query or 'hey' in query or "tara" in query or "hai" in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takecommand()
            app_id = "R776WH-U5PHHEY895"
            client = wolframalpha.Client('R776WH-U5PHHEY895')
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)
            break
        elif "joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            print(ip)
            speak(f"Your ip address is {ip}")

        # elif 'thankyou' in query or 'thanks' in query or 'thank you' in query:
        # break
        elif "take screenshot" in query or "take a screenshot" in query or "capture the screen" in query:
            speak("By what name do you want to save the screenshot?")
            name = takecommand()
            speak("Alright, taking the screenshot")
            img = pyautogui.screenshot()
            name = f"{name}.png"
            img.save(name)
            speak("The screenshot has been succesfully captured")
        elif "show me the screenshot" in query:

            img = Image.open('E://Major Project final//Tarra//' + name)
            img.show(img)
            speak("Here it is ")

        elif "goodbye" in query or "offline" in query:
            print("Alright , going offline. It was nice working with you")
            speak("Alright , going offline. It was nice working with you")
            break


        elif 'stop' in query or "exit" in query or " bye" in query:
            print("Your personal AI assistant Taraa is turning off, good bye")
            speak("Your personal AI assistant Taraa is turning off, good bye")
            break

        elif "translate" in query:

            speak("What do you want to translate?")

            sentence = takecommand()

            speak("Which langauage to translate ?")

            ln = takecommand()
            language=ln.lower()
            print(language)
            if language in LANGUAGES.values():
                translator = Translator()
                result = translator.translate(sentence, src='en', dest=language)
                if result == "None":
                    speak("This langauage doesn't exists")

                else:
                    print(f"In {ln.capitalize()} you would say:")
                    speak(f"In {ln.capitalize()} you would say:")
                    if ln == "hindi":
                        print(result)
                        speak(result.pronunciation)
                    else:
                        print(result.text)
                        speak(result.text)



        elif 'selfie' in query or 'click' in query and 'photo' in query:
            ownerDesignation = "sir"
            speak("Sure " + ownerDesignation + "...")
            clickPhoto()
            speak("clicked")
            print("clicked")
            speak('Do you want to view your clicked photo?',)
            query = takecommand()
            if isContain(query, ['yes', 'sure', 'yeah', 'show me']):
                Thread(target=viewPhoto).start()
                speak("Ok, here you go...")
            else:
                speak("No Problem " + ownerDesignation)

        elif 'map' in query or 'direction' in query:
            if "direction" in query:
                speak('What is your starting location?')
                # fownerDesignation = "sir"
                startingPoint = takecommand()
                speak("Ok " + ownerDesignation + ", Where you want to go?")
                destinationPoint = takecommand()
                speak("Ok " + ownerDesignation + ", Getting Directions...")
                try:
                    distance = webScrapping.giveDirections(startingPoint, destinationPoint)
                    speak('You have to cover a distance of ' + distance)
                    print("You have to cover a distance of ' + distance")
                except:
                    speak("I think location is not proper, Try Again!")
            else:
                # speak('of which city')
                # text = takecommand()
                webScrapping.maps(query)
                speak('Here you go...')

        elif "voice" in query:
            voice_id
            try:
                if 'female' in query:
                    voice_id = 1
                elif 'male' in query:
                    voice_id = 0
                else:
                    if voice_id == 0:
                        voice_id = 1
                    else:
                        voice_id = 0
                engine.setProperty('voice', voices[voice_id].id)
                ownerDesignation = "sir"
                speak("Hello " + ownerDesignation + ", I have changed my voice. How may I help you?")
                # assVoiceOption.current(voice_id)
            except Exception as e:
                print(e)

        elif 'morning' in query or 'evening' in query or 'noon' in query and 'good' in query:
            speak(normalChat.chat("good"))

        elif 'add' in query:
            speak("What do you want to add?")
            item = takecommand()
            ToDo.toDoList(item)
            speak("Alright, I added to your list")

        elif 'show' in query or  'my list' in query:
            items = ToDo.showtoDoList()
            if len(items) == 1:
                speak(items[0])
                print(items[0])
            print('/n'.join(items))



        elif 'whatsapp' in query:
            ownerDesignation = "sir"
            speak("Sure " + ownerDesignation + "...")
            speak('Whom do you want to send the message?')
            rec_phoneno = input()
            speak('What is the message?', )
            message = takecommand()
            Thread(target=webScrapping.sendWhatsapp, args=(rec_phoneno, message,)).start()
            speak("Message is on the way. Do not move away from the screen.")

        elif "time" in query or "date" in query:
            speak(normalChat.chat(query))

        if 'battery' in query or 'system info' in query:
            result = appControl.OSHandler(query)
            if len(result) == 2:
                speak(result[0])
                print(result[1])
                print(result)
            else:
                speak(result)

        elif isContain(query, ['meaning', 'dictionary', 'definition', 'define']):
            result = dictionary.translate(query)
            print(result[1])
            speak(result[1])
            if result[1] == '':
                speak(result[1])

        elif 'volume' in query:
            appControl.volumeControl(query)
            print('Volume Settings Changed')
            speak('Volume Settings Changed')

        elif 'email' in query:
            print("Enter the Reciever Email Id")
            speak('Whom do you want to send the email?')
            rec_email = input()
            speak('What is the Subject?')
            subject = takecommand()
            speak('What message you want to send ?')
            message = takecommand()
            Thread(target=webScrapping.email, args=(rec_email, message, subject,)).start()
            speak('Email has been Sent Succesfully')

        elif isContain(query, ['youtube', 'video']):
            speak("Ok " + ownerDesignation + ", here a video for you...")
            try:
                    speak(webScrapping.youtube(query))
            except Exception as e:
                print(e)
                speak("Desired Result Not Found")
            break

        elif isContain(query,
                     ['factorial', 'log', 'value of', 'math', ' + ', ' - ', ' x ', 'multiply', 'divided by', 'binary',
                      'hexadecimal', 'octal', 'shift', 'sin ', 'cos ', 'tan ']):
            try:
                print(('Result is: ' + math_function.perform(query)))
                speak(('Result is: ' + math_function.perform(query)))

            except Exception as e:
               print(e)

        elif isContain(query, ['news']):
            speak('Getting the latest news...')
            headlines, headlineLinks = webScrapping.latestNews(3)
            for head in headlines: print(head),speak(head)
            print('Do you want to read the full news?')
            speak('Do you want to read the full news?')
            text = takecommand()
            if isContain(text, ["no", "don't" ,"not now"]):
                print("No Problem " + ownerDesignation)
                speak("No Problem " + ownerDesignation)
            else:
                speak("Ok " + ownerDesignation + ", Opening browser...")
                webScrapping.openWebsite('https://indianexpress.com/latest-news/')
                print("You can now read the full news from this website.")
                speak("You can now read the full news from this website.")

        elif isContain(query, ['window', 'close that']):
            appControl.Win_Opt(query)

        if isContain(query, ['tab']):
            appControl.Tab_Opt(query)


        if isContain(query, ['open', 'type', 'save', 'delete', 'select', 'press enter']):
            appControl.System_Opt(query)

        if 'my name' in query:
            speak('Your name is, ' + Name)

        result = normalChat.reply(query)
        if result != "None":
            speak(result)
        else:
            continue
