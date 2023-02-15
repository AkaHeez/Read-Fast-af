import tkinter as tk
from tkinter.filedialog import askopenfilename
import customtkinter as ctk
from PIL import Image
from time import sleep
from threading import Thread
# Create the root window

def saveSettings():
    global wpm, interval
    try:
        wpmL = wpmEntry.get()
        interval = 60/int(wpmL)
        wpm = wpmL
    except:
        interval = 60/wpm
    wpmLabel.configure(text=f"WPM to read at:\n\nCurrent WPM: {wpmL}")
    settings.pack_forget()
    win.pack()

def cancelSettings():
    settings.pack_forget()
    win.pack()

def pauseplayButton():
    global playState
    if playState == "Paused":
        pauseplay.configure(image=pauseI)
        playState = "Playing"
        thread = Thread(target=cycleText)
        thread.start()
    else:
        pauseplay.configure(image=playI)
        playState = "Paused"

def settingsButton():
    win.pack_forget()
    settings.pack()

def rewindButton():
    global wordNum
    wordNum -= 1
    oneWord.configure(text=filetext[wordNum])
    

def fowardButton():
    global wordNum
    wordNum += 1
    oneWord.configure(text=filetext[wordNum])
    
def cycleText():
    global interval, wordNum
    while playState == "Playing":
        sleep(interval)
        oneWord.configure(text=filetext[wordNum])
        wordNum+=1

filepath = askopenfilename() # show an "Open" dialog box and return the path to the selected file
with open(filepath, encoding="utf8") as file:
    filetext = file.read().split()

#Regular Settings
ctk.set_appearance_mode("white")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("900x600")

wpm = 350

#importing things, font and images
playI = ctk.CTkImage(Image.open("icons\play.png"), size=(80, 80))
rewindI = ctk.CTkImage(Image.open(r"icons\rewind.png"), size=(70, 70))
pauseI = ctk.CTkImage(Image.open("icons\pause.png"), size=(80, 80))
fowardI = ctk.CTkImage(Image.open(r"icons\foward.png"), size=(70, 70))
settingsI = ctk.CTkImage(Image.open("icons\settings.png"), size=(70, 70))
my_font = ctk.CTkFont(family="More Sugar", size=30)

#Settings Frame
settings = ctk.CTkFrame(app, width=900, height=600)


wpmVar = ctk.StringVar()
wpmEntry = ctk.CTkEntry(settings,width=300,height=50,border_width=2,font=my_font, corner_radius=10, textvariable=wpmVar)
wpmEntry.place(relx=0.6, rely=0.1, anchor=tk.CENTER)

wpmLabel = ctk.CTkLabel(settings, font=my_font, text=f"WPM to read at:\n\nCurrent WPM: {wpm}")
wpmLabel.place(relx=0.28, rely=0.17, anchor=tk.CENTER)



save = ctk.CTkButton(settings, width=300, height=32, corner_radius=8,fg_color="green", font=my_font, text="Save Settings", command=saveSettings)
save.place(relx=0.7, rely=0.9,anchor=tk.CENTER)
cancel = ctk.CTkButton(settings, width=300, height=32, corner_radius=8,fg_color="red4", font=my_font, text="Cancel", command=cancelSettings)
cancel.place(relx=0.3, rely=0.9,anchor=tk.CENTER)
settings.pack()

#Actual Reading Frame
win = ctk.CTkFrame(app, width=900, height=600)

playState = "Paused"
pauseplay = ctk.CTkButton(win, text="",fg_color="transparent", width= 80, image=playI, command=pauseplayButton)
pauseplay.place(relx=0.5,rely=0.9, anchor=tk.CENTER)
rewind = ctk.CTkButton(win, text="",fg_color="transparent", width= 70, image=rewindI, command=rewindButton)
rewind.place(relx=0.35,rely=0.9, anchor=tk.CENTER)
foward = ctk.CTkButton(win, text="",fg_color="transparent", width= 70, image=fowardI, command=fowardButton)
foward.place(relx=0.65,rely=0.9, anchor=tk.CENTER)
settingsI = ctk.CTkButton(win, text="",fg_color="transparent", width= 70, image=settingsI, command=settingsButton)
settingsI.place(relx=0.94, rely=0.08, anchor=tk.CENTER)

oneWordFont = ctk.CTkFont(family="More Sugar", size=80)
oneWord = ctk.CTkLabel(win, font=oneWordFont, text="Press play to start!")
oneWord.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
wordNum = 0
interval = 60/int(wpm)

# Run the main event loop
app.mainloop()