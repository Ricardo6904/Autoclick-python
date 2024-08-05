import tkinter as tk
import random
import time
import pyautogui
import pickle

# variable para indicar si se está grabando o no
recording = False
positions = []

# función para iniciar la grabación de clics
def start_recording():
    global recording, positions
    recording = True
    positions = []
    input("Presiona Enter para continuar o Cancelar para salir")
    print("Comienza a dar clicks para grabar")
    while recording:
        x, y = pyautogui.position()
        if pyautogui.mouseDown():
            positions.append((x, y))
            print(f"Grabando clic en posición: {x}, {y}")
        if pyautogui.mouseUp():
            pass
    input("Presiona Enter para detener la grabación")
    print("Grabación detenida")
    with open('clicks.pickle', 'wb') as f:
        pickle.dump(positions, f)

# función para detener la grabación de clics
def stop_recording():
    global recording, positions
    recording = False
    print("Grabación detenida")
    # guardar la información de los clics grabados en un archivo
    with open('clicks.pickle', 'wb') as f:
        pickle.dump(positions, f)

# función para iniciar la reproducción de clics
def start_playing():
    print("Se inició la reproducción") #grabados desde el archivo
    with open('clicks.pickle', 'rb') as f:
            positions = pickle.load(f)
            playing = True
global playing
try:
        # cargar la información de los clics
        while playing:
            for x, y in positions:
                pyautogui.click(x, y)
                time.sleep(1) # espera 1 segundo entre cada clic
            # esperar un tiempo aleatorio entre 4 y 6 minutos antes de repetir los clics
            wait_time = random.uniform(4*60, 6*60)
            time.sleep(wait_time)
except FileNotFoundError:
        print("No se encuentra el archivo 'clicks.pickle'")

# función para detener la reproducción de clics
def stop_playing():
    global playing
    playing = False

#crear ventana principal de la interfaz gráfica
root = tk.Tk()
root.title("Automatizador de Clics")
#crear botones para iniciar y detener la grabación
record_button = tk.Button(root, text="Iniciar Grabación", command=start_recording)
stop_record_button = tk.Button(root, text="Detener Grabación", command=stop_recording)

#crear botones para iniciar y detener la reproducción
play_button = tk.Button(root, text="Iniciar reproducción", command=start_playing)
stop_play_button = tk.Button(root, text="Detener reproducción", command=stop_playing)

#agregar botones a la interfaz gráfica
record_button.pack()
stop_record_button.pack()
play_button.pack()
stop_play_button.pack()

root.mainloop()
