import tkinter as tk
import fnmatch
import os
import tkinter.font as font
import pygame
#pip install pygame
from pygame import mixer

run = tk.Tk()
run.title("Vampire Music Player")
run.geometry("400x400")


bg = tk.PhotoImage("yu.png")
position = "C:\\Users\91969\Desktop\music"
design = "*.mp3"

mixer.init()

def select_song():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(position + "\\"+ listBox.get("anchor"))
    mixer.music.play()

def stop_music():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next_music():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get (next_song)
    label.config(text = next_song_name)

    mixer.music.load(position + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_previous_music():
    prev_song = listBox.curselection ()
    prev_song = prev_song[0] - 1
    prev_song_name = listBox.get(prev_song)
    label.config(text = prev_song_name)
    
    mixer.music.load(position + "\\" + prev_song_name)
    mixer.music.play()
    
    listBox.select_clear(0, 'end')
    listBox.activate (prev_song)
    listBox.select_set(prev_song)

def pause_song_music():
    if pauseButton["text"]== "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"

#for side canvas

tum = tk.Canvas (run,width = 290,height = 1000, bg = 'black')

myarc = tum.create_arc (5, 5, 300, 600, start=0, extent=500, fill='red', outline="grey",width=5)
tum.place(relx=.0,rely =.0)
tum = tk.Canvas (run,width=290,height = 1000, bg= 'black')

myarc = tum.create_arc(5,5, 300, 600, start=0, extent=500, fill='red', outline="grey",width=10)
tum.place(relx=.0,rely=.1)
tum = tk.Canvas(run,width = 290,height = 1000, bg = 'black')
myarc = tum.create_arc (5, 5, 300, 600, start=0, extent=500, fill='red', outline="grey",width=5)
tum.place(relx=.0,rely=.2)
tum = tk.Canvas (run,width = 290,height = 1000, bg = 'black')
myarc = tum.create_arc (5, 5, 300, 600, start=0, extent=500, fill='red', outline="grey",width=5)
tum.place(relx=.0,rely=.3)
tum = tk.Canvas (run,width=290,height=1000, bg="black")
myarc = tum.create_arc(5,5, 300, 600, start=0, extent=500, fill = 'red', outline = "grey",width=5)
tum.place(relx=.0,rely=.4)
tum = tk.Canvas (run,width=290,height=1000, bg= 'black')
myarc = tum.create_arc (5,5, 300, 600, start=0,extent=500, fill='red', outline= "grey",width=5)
tum.place(relx=.0,rely=.5)
tum = tk.Canvas (run,width=290,height=1000,bg='black')
myarc = tum.create_arc(5,5, 300, 600,start=0,extent=500, fill="red", outline="grey",width=5)
tum.place(relx = .0,rely =.6)
tum = tk.Canvas(run,width = 290,height = 1000,bg = 'black')
myarc = tum.create_arc (5,5, 300, 600, start=0,extent=500, fill='red', outline="grey",width=5)
tum.place(relx=.0,rely=.7)
tum = tk.Canvas (run, width= 290,height= 1000, bg = 'black')
myarc = tum.create_arc(5,5,300,600,start=0, extent=500, fill='red', outline="grey",width=5)
tum.place(relx =.0, rely=.8)
tum = tk.Canvas (run,width = 290,height = 1000, bg = 'black')
myarc = tum.create_arc (5,5, 300, 600, start=0, extent=500, fill='red', outline="grey",width=5)
tum.place(relx=.0,rely=.9)

#for right side canvas

tum = tk.Canvas (run,width = 290,height = 350,bg = 'blue')
myarc = tum.create_arc(5,5, 300, 600, start = 0, extent=500, fill = 'yellow', outline = "blue",width=10)
tum.place(relx =.77,rely =.0)
tum = tk.Canvas (run,width=290,height = 350,bg= 'blue')
myarc = tum.create_arc(5,5, 300, 600,start = 0, extent = 500, fill = 'yellow', outline="black",width = 10)
tum.place(relx=.77,rely =.1)
tum = tk.Canvas (run,width=290,height=350,bg='blue')
myarc=tum.create_arc(5,5, 300, 600, start=0, extent=500, fill='yellow', outline = "black",width=10)
tum.place(relx=.77,rely=.2)
tum= tk.Canvas (run,width=290,height = 350, bg = 'blue')
myarc = tum.create_arc (5,5, 300, 600, start=0, extent=500, fill='yellow', outline = "black",width=10)
tum.place(relx=.77,rely=.3)
tum  = tk.Canvas (run,width=290,height=350, bg='blue')
myarc =tum.create_arc (5,5, 300, 600, start=0, extent=500, fill='yellow', outline="black",width=10)
tum.place(relx=.77, rely=.4)
tum = tk.Canvas(run,width=290,height=350,bg='blue')
myarc = tum.create_arc(5,5, 300, 600, start=0, extent=500, fill='yellow',outline="black",width=10)
tum.place(relx=.77,rely=.5)
tum = tk.Canvas(run,width=290,height=350,bg='blue')
myarc = tum.create_arc(5,5, 300, 600, start=0, extent=500, fill='yellow', outline ="black",width=10)
tum.place(relx=.77,rely=.6)
tum = tk.Canvas(run,width=200,height=350,bg='blue')
myarc = tum.create_arc(5,5,300,600,start=0, extent=500, fill='yellow', outline="black",width=10)
tum.place(relx=.77,rely=.7)
tum = tk.Canvas(run, width=290,height=350,bg='blue')

myarc = tum.create_arc(5,5,300,600,start=0, extent=500, fill='yellow', outline="black",width=10) 
tum.place(relx=.77, rely=.8) 
tum = tk.Canvas(run,width=290, height=350, bg = 'blue')

myarc = tum.create_arc(5,5, 300, 600, start=8, extent=500, fill='yellow', outline="black",width=10)
tum.place(relx=.77, rely=.9)

font_box = font.Font(family="Helvetica")

listBox = tk.Listbox(run, fg = "black", font=('cambria', 17), bg="pink",width= 50,height=100, highlightcolor='purple', highlightthickness=15)
listBox.pack(padx=45, pady = 35)
#Eg=yellow',

label = tk.Label(run, text= ' ',bg = 'black',fg = 'yellow', font = ('poppins'))
label.pack(pady = 15)

top = tk.Frame(run,bg = "black") 
#(run,bg="black")
top.pack(padx=10, pady=5, anchor = 'center')

prevButton=tk.Button(run, text = "PREVIOUS", bg='white', height=2,width=20, borderwidth=0, highlightcolor='blue', command = play_previous_music)
prevButton.place(x=1000,y=270)
prevButton['font'] = font_box

stopButton = tk.Button(run,text = "STOP",bg = 'red',height=2,width=20,borderwidth=0, 
command = stop_music)
stopButton.place(x=30,y=340)
stopButton['font'] = font_box

playButton = tk.Button(run, text = "PLAY",bg = 'blue',height=2,width=20, 
borderwidth=0, command = select_song)
playButton.place(x=30,y=200)
playButton['font'] = font_box

pauseButton = tk.Button(run, text = "PAUSE",bg = 'yellow',height=2,width=20, 
borderwidth=0, command=pause_song_music)
pauseButton.place(x=30,y=270)
pauseButton['font'] = font_box

nextButton = tk.Button(run, text = "NEXT",bg ='green',height = 2,width = 20, 
borderwidth=0, command = play_next_music)
nextButton.place(x=1000,y=340)
nextButton['font'] = font_box

for root, dirs, files in os.walk(position):
    for filename in fnmatch.filter(files, design):
        listBox.insert('end', filename)


run.mainloop()
