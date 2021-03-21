import os
import requests
from bs4 import BeautifulSoup
import pyautogui
import time

yt_url = 'https://www.youtube.com'


def play_video(song_name):
    url = "https://www.youtube.com/results?search_query="
    tmp = song_name.replace(' ', '+')
    url = url + tmp
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    pyautogui.press('win')
    pyautogui.typewrite('chrome')
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.typewrite(url)
    pyautogui.press('enter')
    time.sleep(5)






