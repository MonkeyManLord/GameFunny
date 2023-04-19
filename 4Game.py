

# #wanted features: spinning, tbag, dancing (eventually), chat spam, random fact paster

        
# #if [ is pressed then spin function
# #if ] is pressed then joke
# #if ' pressed then tbag 
# #if - pressed then chat spam


import keyboard, time, pyautogui, requests, os
from gtts import gTTS

#import json
headers = {
    'Accept': 'application/json',
}

def crouch():
    print('Crouch mode hold: ON')   
    while keyboard.is_pressed('='):
        keyboard.press('c')
        time.sleep(0.1)
        keyboard.release('c')
        time.sleep(0.1)
    print('Crouch mode hold: OFF')
    time.sleep(.3)

#might not work for a while        
def spin():
        print('Spin mode hold: ON')
        while keyboard.is_pressed('['):
            pyautogui.move(-50, 0, 0.05)
        print('Spin mode hold: OFF')
        
def say_joke():
    response = requests.get('https://icanhazdadjoke.com/', headers=headers)
    data = response.json()
    joke = data["joke"]
    
    keyboard.press_and_release('t')
    #keyboard.press_and_release('enter')
    keyboard.write(joke)
    keyboard.press_and_release('enter')
    #print(joke)
    #---------------------SAYING IT
    tts = gTTS(text=joke, lang='ja', tld='co.jp')
    tts.save("new.mp3")
    os.system(f"say '{joke}'")
    os.remove('new.mp3')
    #could try to make program say in voice chat too
        


while True:
    if keyboard.is_pressed('='):
        crouch()
    # if keyboard.is_pressed('['):
    #     spin()
    if keyboard.is_pressed('-'):
        say_joke()

