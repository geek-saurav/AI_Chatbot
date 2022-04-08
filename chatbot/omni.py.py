import speech_recognition as SR
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
from wikipedia.wikipedia import search
from bs4 import BeautifulSoup 
from pywikihow import search_wikihow

run = SR.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# talk method
def talk(text):
    engine.say(text)
    engine.runAndWait()

#talk function
def take_command():
    try:
        with SR.Microphone() as source:
            print('listening...')
            voice = run.listen(source)
            command = run.recognize_google(voice)
            command = command.lower()
            if 'omni' in command:
                command = command.replace('omni', '')
    except:
        pass
    return command


def run_omni():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    
    
    #talk command for time
     
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    
    #talk command for day
    
    elif 'day' in command:
        day = datetime.datetime.now().strftime('%A, %B %d, %Y')
        talk("today's  is" + day)
    
    
    # talk command for searching who the person is
    
    
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)


    #talk command for date        
    
    elif 'date' in command:
        talk('sorry, I have a headache')
    
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    

    #jokes by python module

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
    # talk command for temperature
    

    elif "temperature" in command:
        search = "temperature in bengaluru"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        sav = BeautifulSoup(r.text,"html.parser")
        temp = sav.find("div",class_="BNeawe").text
        talk(f"current {search} is {temp}")

    #talk command for weather    

    elif "weather" in command:
        city  = 'bangaluru'
        url01 = f"https://www.google.com/search?q=weather+{city}"
        f = requests.get(url01).content
        save = BeautifulSoup(f, "html.parser")
        temp1 = save.find("div",attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        data = temp1.split('\n')
        sky = data[1]
        talk(f"current weather of  {city} is {sky}")

    

    #for searching key definitions on google 

    elif "search google" in command:
        import wikipedia as googleSearch
        command = command.replace("omni","")
        command = command.replace("search google","")
        command = command.replace("google","")
        talk("this is what i found on web!")
        pywhatkit.search(command)


        try:
            res = googleSearch.summary(command,2)
            talk(res)

        except:
            talk('data not found!')


 
    elif "how" in command:
        talk("what do you want to know!")
        command = command.replace("omni","")
        command = command.replace("how","")
        how = take_command()
        max_results = 1
        how_to = search_wikihow(how, max_results)
        assert len(how_to) == 1
        how_to[0].print()
        talk(how_to[0].summary)

    #if nothing returns
    
    else:
        talk('Please say it again.')



while True:
    run_omni()