#gtts - google text to speech , it converts the text into audio
##file->setting->project name->project interpreter ->+ ->pygame->install package
from gtts import gTTS
from tkinter import*
from pygame import mixer
root=Tk()
root.geometry("1000x400+0+0")               ##window size
root.title("my text to speech conversion")
root.config(bg="blue")                      ##window color
root.resizable(0,0)
l1=Label(text="Enter your text")
l1.place(x=50,y=20)
mytext=StringVar()                         #***#
def fetch():
    #language='en'
    speech=gTTS(text=mytext.get(),lang='en',slow=False)   #*#
    speech.save("voice6.mp3")
def play():
    mixer.init()                            #mixer.init()- initialises pygame                                         
    mixer.music.load("voice6.mp3")          #mixer.music.load()- loads with music
    mixer.music.play()
e1=Entry(text=mytext,font=('arial',15,'bold'),width=20,bd=10,bg="pink")      #*#
e1.place(x=200,y=10)
b1=Button(text='convert',width=20,command=fetch)                          ##function calling is done by command word
b1.place(x=300,y=200)
b2=Button(text='playfile',width=20,command=play)
b2.place(x=500,y=200)
root.mainloop()                                           ##this culd b played when connected to wifi