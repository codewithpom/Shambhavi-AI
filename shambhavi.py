import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import mail
import pyautogui
import time
import os
import weather_forecast as wf
import subprocess
import webbrowser as web
import cmd_operations
import jokes
import test
import requests
engine = pyttsx3.init()
engine. setProperty("rate", 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()







def default_browser():
    file = open('browser.txt')
    browser = file.read()
    file.close()
    browser = browser.lower()
    return browser

def new_tab():
    pyautogui.keyDown('ctrl')
    pyautogui.press('t')
    pyautogui.keyUp('ctrl')
    time.sleep(4)


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Shambhavi Sir. Please tell me how may I help you")

def takeCommand():
    '''It takes microphone input from the user and returns string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        '''print(e)'''
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()

second = False
on = True
browser = default_browser()
while on :
    # if 1:
        speak("next command")

        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'open wikipedia' in query:
            pyautogui.press('win')
            browser = default_browser()
            pyautogui.typewrite(browser)
            speak('Opening '+browser)
            pyautogui.press('enter')
            time.sleep(5)
            if browser == 'internet explorer':
                new_tab()

            speak('Opening wikipedia')
            pyautogui.typewrite('www.wikipedia.com')
            pyautogui.press('enter')
            time.sleep(4)

        elif 'set time' in query:
            speak('Please enter everythin in 24 hour format')
            speak('Enter hour')
            hour = int(input('Enter hour'))
            speak('Enter minute')
            minute = int(input('Enter minute '))
            speak(cmd_operations.set_time(hour=hour,minute=minute))

        elif 'open whatsapp' in query:
            pyautogui.press('win')
            browser = default_browser()
            pyautogui.typewrite(browser)
            speak('Opening '+browser)
            pyautogui.press('enter')
            if browser == 'internet explorer':
                new_tab()
            time.sleep(6)
            speak('Opening Whatsapp')
            pyautogui.typewrite('web.whatsapp.com')
            pyautogui.press('enter')
            time.sleep(30)

        elif 'open youtube' in query:
            if browser == 'internet explorer':
                web.open('www.youtube.com')
                time.sleep(8)
            else:
                speak('Opening '+browser)
                pyautogui.press('win')
                pyautogui.typewrite(browser)
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.typewrite('www.youtube.com')
                pyautogui.press('enter')
                time.sleep(6)

        elif 'यूट्यूब खोलो' in query:
            if browser == 'internet explorer':
                web.open('www.youtube.com')
                time.sleep(8)
            else:
                speak('Opening '+browser)
                pyautogui.press('win')
                pyautogui.typewrite(browser)
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.typewrite('www.youtube.com')
                pyautogui.press('enter')
                time.sleep(6)

        elif 'open gmail' in query:
            browser = default_browser()
            speak('Opening '+browser)
            pyautogui.press('win')
            time.sleep(0.5)
            pyautogui.typewrite(browser)
            time.sleep(0.5)
            pyautogui.press('enter')
            if browser == 'internet explorer':
                new_tab()
            time.sleep(3)
            speak('Opening Gmail')
            pyautogui.typewrite('www.gmail.com')
            time.sleep(1)
            pyautogui.press('enter')




        elif 'search something on youtube' in query:
            speak('What would you like to search on youtube')
            search = takeCommand()
            speak('Opening '+browser)
            pyautogui.press('win')
            pyautogui.typewrite(browser)
            pyautogui.press('enter')
            if browser == 'internet explorer':
                new_tab()
            time.sleep(5)
            speak('Searching for '+ search +' on youtube')
            pyautogui.typewrite('https://www.youtube.com/results?search_query='+search)
            pyautogui.press('enter')
            time.sleep(1)

        elif 'down' in query :
            pyautogui.press('down', 7)


        elif 'now' in query:
            pyautogui.press('down',7)

        elif 'up' in query:
            pyautogui.press('up' ,7 )

        elif 'app' in query:
            pyautogui.press('up',7)


        elif 'open google' in query:
            pyautogui.press('win')
            speak('Opening '+browser)
            pyautogui.typewrite(browser)
            pyautogui.press('enter')
            time.sleep(4)
            if browser == 'internet explorer':
                new_tab()

            speak('Opening google')
            pyautogui.typewrite('www.google.com')
            pyautogui.press('enter')

        elif 'open stack overflow' in query:
            speak('Opening '+browser)
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.typewrite(browser)
            pyautogui.press('enter')
            if browser == 'internet explorer':
                new_tab()

            speak('Opening stackoverflow')
            time.sleep(7)
            pyautogui.typewrite("stackoverflow.com")
            pyautogui.press('enter')




        elif 'play music' in query:
            music_dir = 'C:\\Users\\Public\\Music\\Sample Music'
            songs = os.listdir(music_dir)
            number = len(songs)
            print(songs)
            i = -1
            while i < number-1:
                i = i + 1
                file_name = songs[i]
                file_location = music_dir +'\\'+file_name
                os.startfile(file_location)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print({strTime})



        elif 'open chrome' in query:
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.typewrite('chrome')
            pyautogui.press('enter')
            speak('Opening Chrome')
            print('Opening Chrome')

        elif 'send email' in query:
            try:

                speak('To whom do you want to send this mail ')
                to = takeCommand().lower()
                if os.path.exists('contacts/'+to+'.txt'):
                    to = open('contacts/' +to + ".txt", 'r')
                    to = to.readlines()
                    reciever = to[1]
                    speak('What will be the subject')
                    subject = takeCommand()
                    speak('What will be the message')
                    message = takeCommand()
                    mail.send_email(to, subject, message)
                    speak("Email has been sent!")

                else:
                    speak('No such contact')
                    print('No such contact')
            except Exception as e:
                print('Sorry mail could not be sent')
                print(e)
                speak("Sorry sir")

        elif "exit" in query or 'close this window' in query:
            speak('Are you sure you want to exit')
            confirm = takeCommand()
            if confirm == 'yes':
                pyautogui.keyDown('alt')
                pyautogui.press('f4')
                pyautogui.keyUp('alt')



        elif 'open a website' in query:
            speak('Which website would you like to visit say without the .com extension')
            website = takeCommand()
            website = website.lower()
            speak('Opening '+browser)
            pyautogui.press('win')
            pyautogui.typewrite(browser)
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(2)
            if browser == 'internet explorer':
                new_tab()
            speak('Opening'+website+".com")
            time.sleep(0.5)
            pyautogui.typewrite(website+'.com')
            pyautogui.press('enter')

        elif 'calculate' in query:
            speak('Say the operation')
            equation = takeCommand()
            if 'multiplication' in equation:
                speak('Say the first number')
                first_number = int(takeCommand())
                speak('Say the second number')
                second_no = int(takeCommand())
                result = first_number * second_no
                result = str(result)
                print('The result is '+result)
                speak('The result is '+result)

            elif 'addition' in equation:
                speak('So you want to add somethings na')
                speak('Say the first number')
                first_number = int(takeCommand())
                speak('Say the second number')
                second_no = int(takeCommand())
                result = first_number + second_no
                result = str(result)
                print('The result is '+result)
                speak('The result is '+result)

        elif 'minimise' in query:
            speak('Minimizing this window')
            pyautogui.keyDown('win')
            pyautogui.press('d')
            pyautogui.keyUp('win')

        elif 'switch between' in query:
            speak('Switching between')
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')

        elif 'make this window small' in query:
            speak('Making this window small')
            pyautogui.keyDown('win')
            pyautogui.press('down')
            pyautogui.keyUp('win')

        elif 'make this window big' in query:
            speak('Making this window bigger')
            pyautogui.keyDown('win')
            pyautogui.press('up')
            pyautogui.keyUp('win')


        elif'change name' in query:
            speak('What should i call you then')
            name = takeCommand()
            file = open("name.txt",'w')
            file.write(name)

        elif 'open a program' in query:
            speak('Which program would you like to open sir')
            program = takeCommand()
            pyautogui.press('win')
            pyautogui.typewrite(program)
            pyautogui.press('enter')

        elif 'increase volume' in query:
            speak('Increasing volume')
            pyautogui.press('volumeup')

        elif 'decrease volume' in query:
            speak('Decreasing volume')
            pyautogui.press('volumedown')

        elif 'volume mute' in query:
            pyautogui.press('volumemute')
            speak('Volume muted')

        elif 'mute volume' in query:
            pyautogui.press('volumemute')
            speak('Volume muted')

        elif 'message' in query:
            speak('To whom will you like to send this message')
            reciever = takeCommand()
            if os.path.exists('contacts/'+reciever+'.txt'):
                file = open('contacts/'+reciever+'.txt','rt')
                data = file.readlines()
                no = data[0]
                print('Recievers number' +no)
                print('Recievers name' + reciever)
                speak('What will be the message')
                message = takeCommand()
                time_hour = hour = int(datetime.datetime.now().hour)
                time_minute = int(datetime.datetime.now().minute)
                time_minute = time_minute + 1
                time_minute = int(time_minute)
                if time_hour < 10:
                    time_hour = str(time_hour)
                    time_hour = time.replace('0','')
                    time_hour = int(time_hour)

                pyautogui.press('win')
                time.sleep(1)
                pyautogui.typewrite('chrome')
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.typewrite('https://web.whatsapp.com/send?phone=' + no + '&text=' + message)
                time.sleep(25)
                pyautogui.press('enter')


                if datetime.datetime.now().minute == time_minute:
                    time.sleep(6)
                    pyautogui.press('enter')




        elif 'show sent in gmail' in query:
            speak('Opening '+browser)
            pyautogui.press('win')
            pyautogui.typewrite(browser)
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(5)
            if browser == 'internet explorer':
                web.open('https://mail.google.com/mail/u/0/#sent')
            speak('Opening sent in Gmail')
            pyautogui.typewrite('https://mail.google.com/mail/u/0/#sent')
            pyautogui.press('enter')

        elif 'make contact' in query:
            speak('Name of the contact')
            name = takeCommand()
            speak('What is the e- MAIL ADDRESS')
            email = input('What is the E mail address')
            speak('What is the phone number with country code')
            number = input('What is the phone number')
            file_name = name+'.txt'
            file_location = 'contacts/'+file_name
            file = open(file_location,'a')
            file.write(number+'\n')
            file.write(email)

        elif 'weather' in query or 'weather forecast' in query:
             whether =wf.forecast(place="Muzaffarpur")
             place = whether['place']
             time = whether['time']
             dat = whether['date']
             day = whether['day']
             day_temperature = day['temperature']
             day_precipitate = day['precipitate']
             day_uv_description = day['uv_description']
             day_windspeed = day['wind_speed']
             day_humidity = day['humidity']
             day_phrase = day['phrases']
             day_narrative = day['narrative']
             print('Location:'+place)
             speak('Location is '+place)
             print('Time:'+time)
             speak('The time is '+time)
             print('Date:'+dat)
             speak('The date is'+dat)
             print("Day's report:")
             speak('Days report is')
             print('Temperature:'+str(day_temperature)+'ºC')
             speak('The temperature is '+str(day_temperature)+'degree Celsius')
             print('Precipitation:'+str(day_precipitate)+'%')
             speak('The precipitation level is'+str(day_precipitate)+'percent')
             print('UV description:'+str(day_uv_description))
             speak('The UV description is'+str(day_uv_description))
             print('Wind speed:'+str(day_windspeed)+'km/h')
             speak('The Wind speed is'+str(day_windspeed)+'kilometer per hour')
             print('Humidity:'+str(day_humidity)+'%')
             speak('Humidity'+str(day_humidity)+'percent')
             print('Condition in one line:'+str(day_phrase))
             speak('Condition in one line '+str(day_phrase))
             print('Narrative:',str(day_narrative))
             speak('Narrative '+str(day_narrative))
             print('Night report')
             speak('Night report')
             day = whether['night']
             day_temperature = day['temperature']
             day_precipitate = day['precipitate']
             day_uv_description = day['uv_description']
             day_windspeed = day['wind_speed']
             day_humidity = day['humidity']
             day_phrase = day['phrases']
             day_narrative = day['narrative']
             print('Temperature:'+str(day_temperature)+'ºC')
             speak('The temperature is '+str(day_temperature)+'degree Celsius')
             print('Precipitation:'+str(day_precipitate)+'%')
             speak('The precipitation level is'+str(day_precipitate)+'percent')
             print('UV description:'+str(day_uv_description))
             speak('The UV description is'+str(day_uv_description))
             print('Wind speed:'+str(day_windspeed)+'km/h')
             speak('The Wind speed is'+str(day_windspeed)+'kilometer per hour')
             print('Humidity:'+str(day_humidity)+'%')
             speak('Humidity'+str(day_humidity)+'percent')
             print('Condition in one line:'+str(day_phrase))
             speak('Condition in one line '+str(day_phrase))
             print('Narrative:',str(day_narrative))
             speak('Narrative '+str(day_narrative))



        elif 'disconnect wi-fi' in query:
            os.system('netsh wlan disconnect')
            print('Disconnected')
            speak('Disconnected')

        elif 'open dvd' in query:
            import DVD
            speak('Opening DVD player')
            DVD.open()
            time.sleep(10)
            speak('Closing DVD player')
            DVD.close()

        elif 'search for something on google' in query:
            speak('What would you like to search')
            question = takeCommand()
            speak('Opening '+browser)
            pyautogui.press('win')
            pyautogui.typewrite(browser)
            pyautogui.press('enter')
            if browser == 'internet explorer':
                new_tab()
            time.sleep(6)
            pyautogui.typewrite('www.google.com/search?q='+question)
            pyautogui.press('enter')

        elif 'connect wi-fi' in query:
            speak('Enter wifi interface name')
            name = input('What is the interface name')
            try:
                os.system('netsh wlan connect '+name)

            except Exception as e:
                speak('Sorry')
                speak('the reason is '+ e)


        elif 'wikipedia' in query:
                query = query.replace('wikipedia' ,'')
                result = wikipedia.summary(query,3)
                print(result)
                speak(result)

        elif 'show wi-fi' in query:
            devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
            devices = devices.decode('ascii')
            devices = devices.replace("\r", "")
            print(devices)
            speak(devices)


        elif 'open space x' in query:
            speak('Opening '+browser)
            pyautogui.press('win')
            pyautogui.typewrite(browser)
            pyautogui.press('enter')
            if browser == 'internet explorer':
                new_tab()
            speak('Opening '+browser)
            time.sleep(4)
            pyautogui.typewrite('https://www.spacex.com/')
            speak('Opening spacex.com')
            pyautogui.press('enter')
            time.sleep(7)

        elif 'open tesla' in query:
            speak('Opening '+browser)
            pyautogui.press('win')
            pyautogui.typewrite(browser)
            pyautogui.press('enter')
            if browser == 'internet explorer':
                new_tab()
            time.sleep(4)
            speak('Opening tesla')
            pyautogui.typewrite('https://www.tesla.com/')
            pyautogui.press('enter')
            time.sleep(7)

        elif 'is my ideal' in query:
            file = open('detail/ideal.txt','r')
            ideal = file.read()
            file.close()
            print('Your ideal is '+ideal)
            speak('Your ideal is '+ideal)

        elif 'about my ideal' in query:
            file = open('detail/ideal.txt','r')
            ideal = file.read()
            file.close()
            print('Your ideal is '+ideal)
            speak('Searching wikipedia')
            result = wikipedia.summary('elon musk', 6)
            print(result)
            result = str(result)
            speak('According to wikipedia '+'about your ideal '+ideal +result)


        elif 'open windows explorer' in query:
            os.startfile('C:\Windows\explorer.exe')
            time.sleep(5)

        elif 'open brave' in query:
            pyautogui.press('win')
            pyautogui.typewrite('brave')
            pyautogui.press('enter')
            time.sleep(10)

        elif 'open firefox' in query:
            pyautogui.press('win')
            pyautogui.typewrite('firefox')
            pyautogui.press('enter')
            time.sleep(6)



        elif 'open internet explorer' in query:
            pyautogui.press('win')
            pyautogui.typewrite('internet explorer')
            pyautogui.press('enter')
            time.sleep(10)


        elif 'stop yourself' in query:
            speak('Ok sir i am going to sleep bit you can call me by saying Shambhavi bye bye sir ')
            second = True
            on = False

        elif 'new tab' in query:
            speak('Making new tab')
            new_tab()

        elif 'tell me a joke' in query:
            speak(jokes.jokes())
            print(jokes.jokes())

        elif 'open cmd' in query:
            pyautogui.keyDown('win')
            pyautogui.press('r')
            pyautogui.keyUp('ctrl')
            pyautogui.typewrite('cmd.exe')
            pyautogui.press('enter')
            time.sleep(5)

        elif 'open command prompt' in query:
            pyautogui.keyDown('win')
            pyautogui.press('r')
            pyautogui.keyUp('win')
            pyautogui.typewrite('cmd.exe')
            pyautogui.press('enter')
            time.sleep(5)

        elif 'open dos' in query:
            pyautogui.keyDown('win')
            pyautogui.press('r')
            pyautogui.keyUp('ctrl')
            pyautogui.typewrite('cmd.exe')
            pyautogui.press('enter')
            time.sleep(5)

        elif 'set date' in query:
            speak('Enter day')
            day = int(input('Enter date'))
            speak('Enter month')
            month = int(input('Enter month digit'))
            speak('Enter year')
            year = int(input('Enter year'))
            print(cmd_operations.set_date(day=day,month=month,year=year))
            speak(cmd_operations.set_date(day, month, year))


        elif 'play this' in query:
            pyautogui.press('enter')



        elif 'play' in query:
            query = query.replace('play','')
            test.play_video(query)
            time.sleep(3)
            pyautogui.press('tab')
            time.sleep(5)

        elif 'next video' in query:
            pyautogui.press('tab',4)

        elif 'value of bitcoin' in query:
            x = requests.get('https://api.coincap.io/v2/assets')
            info = x.json()['data'][0]
            print('The name is '+info['id'])
            speak('The name is'+info['id'])
            print('The rank is '+info['rank'])
            speak('The rank is '+info['rank'])
            value = 'The symbol is '+info['symbol']
            print(value)
            speak(value)
            value = 'The max supply is '+info['maxSupply']
            print(value)
            speak(value)
            value = 'The market capital in usd is '+info['marketCapUsd']
            print(value)
            speak(value)
            value = 'The price change in 24 hours is '+info['changePercent24Hr']
            print(value)
            speak(value)
            value = 'The price of each stock is '+info['priceUsd']
            print(value)
            speak(value)









while second:
    command = takeCommand().lower()
    print(command)

    if 'shambhavi' in  command:
        speak('I am back sir')
        pyautogui.keyDown('shift')
        pyautogui.press('f10')
        pyautogui.keyUp('shift')
        pyautogui.press('enter')
        os.startfile('shambhavi.py')


    elif 'shut down yourself' in command:
        speak('I am going forever I cannot go by leaving you.But I am going.Bye bye sir.')
        break