import pruebCLick
import tkinter as tk
#codigo fuer afuncion

root = tk.Tk()
root.geometry("300x200")
root.title("Click Recorder")

record_button = tk.Button(root, text="Record clicks", command=pruebCLick.start)
record_button.pack()


replay_button = tk.Button(root, text="Play clicks", command=pruebCLick.rep)
replay_button.pack()

root.mainloop()

#160, 20
#1237, 496
#1234, 491
