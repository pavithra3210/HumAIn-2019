from playsound import *
from gtts import *
import os
from time import *
import random
import requests
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import webbrowser


def play(b):
    global i
    tts = gTTS(text = b, lang = 'en')
    i+=1
    z = "voice"+str(i)+".mp3"
    tts.save(z)
    print(b)
    playsound(z)
    os.remove(z)

def hello():
    a = ["what can i do for you","how can i help you"]
    b=random.choice(a)
    play(b)

def opens(x):
    if 'calculator' in x:
            os.system('start calc.exe')
    elif 'notepad' in x:
            os.system('start notepad.exe')
    elif 'chrome' in x:
            os.system('start chrome.exe')
    elif 'settings' in x:
            os.system('start control.exe')
    elif 'cmd' in x or 'command' in x:
            os.system('start cmd.exe')
    elif 'word' in x:
            os.system('start winword.exe')
    elif 'powerpoint' in x or 'ppt' in x:
            os.system('start powerpnt.exe')
    elif 'excel' in x or 'ppt' in x:
                os.system('start excel.exe')

def enquire(x):
    if "weather" in x:
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        city = input('city name:')
        url = api_address + city
        json_data = requests.get(url).json()
        formatted_data = json_data['weather'][0]['main']
        temp = json_data['main']['humidity']
        temp1 = json_data['main']['temp_max']
        b = "the weather condition in "+city+" is "+formatted_data.lower()+"\nthe humidity level is "+str(temp)+"\nthe temperature is around "+str(temp1)
        play(b)

    elif "Train Status" in x:
        api_address='http://indianrailapi.com/api/v2/PNRCheck/apikey/<63dae4d7b7eadfc066aeea06379c197e>/PNRNumber/<6431669781>/Route/1/'
        prn = input('PRN Number:')
        url = api_address + prn
        json_data = requests.get(url).json()
        formatted_data = json_data['status'][0]['time']
        temp = json_data['status']['time']
        temp1 = json_data['main']['temp_max']
        b = "the train "+prn+" is  "+str(temp)+"\nthe time is around "+str(temp1)
        play(b)

    elif "news" in x:
        news_url="https://news.google.com/news/rss"
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        for news in news_list[0:5]:
            b=news.title.text
            play(b)
            print('-'*50)
        '''b = "do you want to read the news?"
        play(b)
        if "yes" == input():
            b = "which news you want to read?"
            play(b)
            if '1' in input():
                

        else:
            break'''
            

    elif "open" in x:
        opens(x)

    elif "youtube" in x:
        b = "what do you want to search in youtube?"
        play(b)
        text = input()
        b = "here is your result"
        play(b)
        webbrowser.open("https://www.youtube.com/results?search_query="+text)

    elif "gmail" in x:
        b = "do you want to sign in or create account in gmail?"
        play(b)
        if "sign" in input():
            b = "here is your result"
            play(b)
            webbrowser.open("https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1")
            
        elif "create" in input():
            b = "here is your result"
            play(b)
            webbrowser.open("https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en")


    elif "song" in x:
        playsound('123.mp3')

    elif "time" in x:
        play(ctime())

    elif "how are you" in x:
        a=['i am fine','wonderful thanks','so happy you asked','i am doing great','i am feeling lucky']
        b=['what can i do for you','how can i help you','do u need any information']
        play(random.choice(a))
        play(random.choice(b))

    elif "parents" in x:
        b = "engineers who delevoped me are my parents"
        play(b)

    elif "birthday" in x:
        b = "it was almost 1 month back"
        play(b)

    elif "i love you" in x:
        a=['i love you too','i cant measure how much i love you','you are my best partner']
        play(random.choice(a))
        
    elif "marry" in x:
        a=['i am already in a committed relationship as your assistant','i promise to be your assistant forever','i finally found the dream i have been searching for to be your assistant']
        play(random.choice(a))

        
    else:
        import webbrowser
        ie = webbrowser.get(webbrowser.iexplore)
        ie.open('https://www.google.com/search?source=hp&ei=ed9eW4KvLYrNvgSJ4aeIDg&q='+x)      


def pepper():
    name = ['pepper','hi pepper','hello pepper']
    if input() in name:
        b = "hi aravind"
        play(b)
        if strftime("%H") < "12":
            a = ["good morning","happy morning","beautiful morning","precious morning"]
            b=random.choice(a)
            play(b)
        elif strftime("%H") < "16":
            a = ["good noon","happy noon","beautiful noon","precious noon"]
            b=random.choice(a)
            play(b)
        elif strftime("%H") < "19":
            a = ["good evening","happy evening","beautiful evening","precious evening"]
            b=random.choice(a)
            play(b)
    else:
        print('ERROR 404')

i=0
pepper()
while 1:
    hello()
    x = input()
    enquire(x)
    b = "do you want to continue"
    play(b)
    z = input()
    if "yes"==z.lower() or "s" ==z.lower():
        continue
    else:
        break
        
    
