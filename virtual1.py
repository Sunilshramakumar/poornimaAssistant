from urllib.request import urlopen
from matplotlib.pyplot import specgram
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import wolframalpha
import os
import time
# import vlc
# import pafy
import subprocess
from ecapture import ecapture as ec
import json
import requests
from datetime import date

print('Loading your Personal Assistant - Poornima Assistant')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Check me, please say that again")
            return "None"
        return statement

speak("Loading your Personal Assistant - Poornima Assistant")
wishMe()
speak("I have an information of Faculties, Current today calender, The upcoming events or the most importantly the today latest news!!")
speak("so for the information of faculty You have to speak faculty name, for event information you have to speak event name, and for the notice say notice and for the calendar speak today's calendar. And for the other stuff u can speak open google, youtube, stackflow etc.")


query3 = requests.get('http://127.0.0.1:8000/api/notice/')
query4 = requests.get('http://127.0.0.1:8000/api/calendar/')



if __name__=='__main__':
    while True:
        speak("Tell me how can I help you now?")
        speak("Now speak what would you like to ask!!")
        statement = takeCommand().lower()
        query1 = requests.get('http://127.0.0.1:8000/api/assistant/')
        query2 = requests.get('http://127.0.0.1:8000/api/event/')
        query3 = requests.get('http://127.0.0.1:8000/api/notice/')
        query4 = requests.get('http://127.0.0.1:8000/api/calendar/')

        # for  all professor data
        lst1 = query1.json()
        for i in lst1:
            if statement == i.get('name').lower():
                speak('Welcome I want to tell you about the: ' +i.get('name'))
                speak('the designation of the: Faculty:' +i.get('name')+ 'is' +i.get('designation')+ 'And i must say that this faculty is best in their work.')
                speak('And the Email id of this faculty:' +i.get('name')+ 'You can contact with this faculty with the help of this Email:' +i.get('email'))
                speak('So now i want to tell you some specialization of : ' +i.get('name')+ 'are' +i.get('specialization'))
                speak('And the Achivements of the Faculty :' +i.get('name')+ 'are' +i.get('achivements'))



        lst2 = query2.json()
        for i in lst2:
            if statement == i.get('ename').lower():
                speak('Welcome I want to tell you about the event:' +i.get('ename'))
                speak('The organizers of the Event are :' +i.get('eorganizers'))
                speak('So now i want to tell you some discription of the event:' +i.get('ediscription'))
                speak('So the coordinators of the event are:' +i.get('ecoordinators')+ 'If u want some other information u can contact with them.')


        if statement in 'notice':
            lst3 = query3.json()
            today = str(date.today())
            for i in lst3:
                if today == i.get('date'):
                    speak('today"s notices is like ')
                    speak(i.get('notice'))
        if statement in 'Notice':
            speak('Do you want notice"s from college , or other notice"s from google')

        # for calender
        if statement in "today's calendar":
            lst4 = query4.json()
            today = str(date.today())
            for i in lst4:
                if today == i.get('date'):
                    speak('today"s calender is like ')
                    speak(i.get('purpose'))

        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Poornima assistant is shutting down,Good bye')
            print('your personal assistant Poornima assistant is shutting down,Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =("wikipedia", "")
            results = wikipedia.summary(f'{statement}', sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'chairman of college' in statement:
            speak('Mister SashiKant Singhi is the Chairman of Poornima Group. Mister Shashikant Singhi is B.Arch. (Honors) from J.J. College of Architecture, Mumbai.  ')
            speak('He has professional expertise and wide ranging experience in various prestigious assignments for designing and construction of institution, public buildings and industrial houses.')
            speak('Shri. Shashikant Singhi was actively involved in architecture and project management consultancy during 1985-1999 in Jaipur. ')
        
        elif 'director of college' in statement:
            speak('Mister Rahul Singhi is the Director of the Poornima Group. Mr. Rahul Singhi is the Co-Founder, Poornima University & Director, Poornima Group. He believes in the ideology of giving back to society and brings the same into action via educating students. ')
            speak('In this interview he talks about the leadership style he follows, and how with an open mind it is easy to assess situations.')
            speak(' Also, he focuses on the programs the university has to offer and how the university is aimed to move forward by achieving the mark of excellence in teaching, research and placements.')
        
        elif 'principal of college' in statement:
            speak('Dr. Dinesh Goyal is working as Principal at revered Institute, namely Poornima Institute of Engineering & Technology.   He has been instrument in obtaining accreditations for his institutions, from various agencies like NAAC & NBA, He has received Grants for Research, Development, Conference & workshops worth Rs. 24 Lakh, from agencies like AICTE, TEQIP etc. He has been awarded by “Elets Excellence Award 2017” at Higher Education & Human Resource Conclave by Higher Education Department of Government of Rajasthan.')
            speak('Acquiring an experience of 20 years in teaching, and perceive keen interest in research area relating Cloud Security, Image Processing and Information Security.')
            speak('With a mission to append more and better skill set, has organized short term training programs as Convener and Co-Convener within during this short career span.')
        
        elif 'department of college' in statement:
            speak('Hii i want to tell about department in our college is that. The computer Engineering department.  which is related to develop competent professional with innovative mindset, problem solving, design and implementation skills through excellent education.')
            speak('The Civil engeeniring department, The Department of Civil Engineering has an excellent and rich history and an outstanding record of contributions to the profession and community. The department is well recognized for excellence in facilities and teaching. Department offers B.Tech. programs in the area of Civil Engineering.')
            speak('the Electrical Engineering department, The Department of Electrical Engineering is started in year 2007 with an intake 60 students. The Department of Electrical Engineering is a blend of teaching and research activities pertaining to Electrical Engineering prospective. At present the Department offers B. Tech. degree in Electrical Engineering as per Rajasthan Technical University prospective.')
            speak('the Department of Electronics & Communication Engineering, the ECE department started in 2019 under School of Engineering and Technology. The primary goal to start this program is to produce highly skilled young engineers so that they can contribute in the various industry and academy jobs. Our course curricular is designed in such a way that the students can get a strong foundation in both theoretically and practically in the field of ECE.')

        elif 'facilities in college' in statement:
            speak('The facilities which poornima provides you is that The best Laborities as machine drawing lab, physics lab, Computer Lab, Language lab for the first year department. Online examination lab is located on the ground foor of the new building. IBM Lab for research on Business Intelligence and Cloud Computing is located on the second floor of the Engineering block.')
            speak('The another facilities of poornima is Library which is Soul of PIET.')
            speak('The Auditorium, The most earning weather of all the feathers of PF block is ARBUDA CONVENTION CENTRE located at PIET Campus.')
            speak('Transportation, Biggest fleet of 10 new Swaraj Mazda buses operating from all corners of Jaipur owned by PIET. Well coordinated, time bounded and regular service available throughout the year.')
            speak('Mess,Canteen,Provision Store, Canteen: 200 Students Mess: 500 Students Kitchen equipped with chapatti maker machine, deep freezer, grinder and other modern kitchen aids.The College Campus offers an excellent choice of food to eat. Each campus houses a Campus Canteen, which offer delicious food, superior services with innovative practices.')
            speak('Basketball/Volleyball court, The new building also comprises of an open theatre area including well-facilities like canteen, a Basketball court and Volleyball court.')
            speak('GYM Facility, The new building also comprises of an open theatre area including well-facilities like canteen, a Basketball court and Volleyball court.')
            speak('Medical Facility, MOU with MGH for all medical facilities (0.5 km far from institute) Equipped Medical Room, Dedicated vehicle in campus ,Routine checkup by Medical practitioner')
            speak('Solar Water Heater,24000 Litre/day.')
            speak('These all are the facilities which is provided by our organization.')
            speak('Thank You')

        elif 'activities in college' in statement:
            speak('There is a lot of activity which is organized by student council of Poornima. The clubs which are include in these activities are.'
            'Aptinus Club, Codium club, cytron club which all of these related to your coding skills uyour mindset, electrinfiny club, engineering and career awareness club,'
            'Enterprenurship club for your ideas, green club , placement club, robotics club for your creation, sports club, dance club, music activity, All these things which are related to the activity of the students.'
            'For all these club has a particular teacher or faculty coordinator in which under that all the student council members work for the students.'
            'Thank You!!')

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Poornima Assistant point O your persoanl assistant. I am programmed to minor tasks like'
                  'Describing college faculties, The upcoming events, The special notice, or calendar information or youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Strikers Team PGI 4th year 2022 Batch CS Branch. The creators was 'Saloni Jain', 'Sunil Sharma', 'Mohan Gayen'")
            print("I was built by team Strikers")

        elif "stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak(news)
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "where is" in statement:
            statement = statement.replace("where is", "")
            location = statement
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 

        # elif "camera" in statement or "take a photo" in statement:
        #     ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)


            # E2UGH2-86WWUALPJW
            # weather information
            # APPID: E2UGH2-A7HE6H65TQ


        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="E2UGH2-5JPUJ7TGRU"
            

            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        
        elif 'weather information' in statement:
            speak('I can answer all the deatils of weather')
            question=takeCommand()
            app_id2 = "E2UGH2-A7HE6H65TQ"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)











