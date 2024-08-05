import tkinter as tk
from pynput import mouse

clicks = []

def on_click(x, y, button, pressed):
    if pressed:
        clicks.append((x, y))

def start_recording():
    global listener
    listener = mouse.Listener(on_click=on_click)
    listener.start()

def stop_recording():
    listener.stop()
    with open("clicks.txt", "w") as f:
        for click in clicks:
            f.write("X: {}, Y: {}\n".format(click[0], click[1]))

root = tk.Tk()
root.geometry("300x200")
root.title("Click Recorder")

record_button = tk.Button(root, text="Grabar clicks", command=start_recording)
record_button.pack()

stop_button = tk.Button(root, text="Detener grabación", command=stop_recording)
stop_button.pack()

root.mainloop()