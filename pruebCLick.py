import time
import random
from pynput import mouse
import pyautogui
import tkinter as tk
import datetime

clicks = []

def start_recording(x, y, button, pressed):
    if pressed:
        print(x,y)
        clicks.append((x, y))
        with open("clicks.txt", "a") as f:
            f.write("{}, {}\n".format(x, y))
            f.flush()

def start():
    pyautogui.PAUSE = 0.001
    pyautogui.FAILSAFE = True
    pyautogui.hotkey('ctrl', 'alt', 'p')
    pyautogui.hotkey('ctrl', 'alt', 's')
    with mouse.Listener(on_click=start_recording) as listener:
        listener.join()

def replay_clicks(current_time, delay):
    print("Tiempo de demora", (delay/60) ,"Hora actual", current_time)
    with open("clicks.txt", "r") as f:
        try:
            clicks = [tuple(map(int, line.strip().split(','))) for line in f]
        except ValueError:
            print("Hay una línea en blanco en el archivo, se ignorará.")
    for x, y in clicks:
        pyautogui.click(x, y)
        time.sleep(random.uniform(3*60, 3.4*60))

def rep():
    while True:
        current_time = datetime.datetime.now()
        delay = random.uniform(1, 2)
        replay_clicks(current_time, delay)
        time.sleep(delay)