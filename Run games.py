import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog, Text 
import os

root = tk.Tk()
apps = []

root.title("run games V.12")




def addApp():

    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="/", title="Select game",
                                          filetypes=(("exe games", "*.exe"),("All files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="#233067")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)
        

def saveFile():
    file = filedialog.asksaveasfile(defaultextension=".exe",)
    
    
label = tk.Label(root, text="RUN GAMES V.12", font=("arialblack"), bg="#1c0142")
label.pack()

canvas = tk.Canvas(root, height=700, width=700, bg="#1e0036")
canvas.pack()

frame = tk.Frame(root, bg="#540194")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


saveFile = tk.Button(root, text="save games", padx=10,
                     pady=5, fg="#4600c7", bg="#1c0142", command=saveFile)
saveFile.pack()


openFile = tk.Button(root, text="Open game", padx=10,
                     pady=5, fg="#4600c7", bg="#1c0142", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run game", padx=10,
                     pady=5, fg="#4600c7", bg="#1c0142", command=runApps)
runApps.pack()

    




for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()

with open("save games.txt", "w") as f:
    for app in apps:
        f.write(app + ",")
