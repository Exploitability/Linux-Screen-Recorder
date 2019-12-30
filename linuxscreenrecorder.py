#Author: Andrew Otto B
#If you're looking for a skilled Python, C++, Java, C#, or JavaScript developer
#Contact me: twitter.com/@ARPPoisoning

#Guide for Debian/Ubuntu-based distributions. If you're using a Arch-based distribution, replace apt-get with pacman.
#Prequisites:
#sudo apt-get install ffmpeg
#sudo apt-get install python-tk
#sudo apt-get install python-pil
#sudo apt install python-pip
#pip install pyscreenshot
#pip install pyscreenshot


from Tkinter import *
from threading import Thread
from os.path import expanduser
import os
import time
import tkFont
import pyscreenshot

def recThread():
        os.system("ffmpeg -video_size 1366x768 -framerate 30 -f x11grab -i :0.0 -f pulse -ac 2 -i 0 $(date +%d%b_%Hh%Mm).mkv")
def rec():
        b.config(state=DISABLED)
        b1.config(state=ACTIVE)
        t = Thread(target=recThread)
        t.start()
        global count_flag, secs, mins
        count_flag = True
        secs=0
        mins=0
        while True:
                if count_flag == False:
                        break
                label['text'] = str("%02dm:%02ds" % (mins,secs))
                if secs == 0:
                        time.sleep(0)
                else:
                        time.sleep(1)
                if(mins==0 and secs==1):
                        b1.config(bg="red")
                        b.config(fg="red")
                        b.config(bg="red")
                if secs==60:
                        secs=0
                        mins+=1
                        label['text'] = str("%02dm:%02ds" % (mins,secs))
                root.update()
                secs = secs+1
def stop():

        b.config(state=ACTIVE)
        b1.config(state=DISABLED)
        b1.config(fg="green")
        b1.config(bg="green")
        b.config(fg="green")
        b.config(bg="green")
        global count_flag
        count_flag = False
        os.system("pkill -n ffmpeg")
        try:
            t.stop()
        except:
            print("")

def screenshot():
        im = pyscreenshot.grab()
        im.save('screenshot.png')

             

root = Tk()
fontTime = tkFont.Font(family="Franklin Gothic", size=12)
fontButton = tkFont.Font(family="Times New Roman", size=11,weight="bold")
label = Label(root, text="00m:00s",fg="blue",font="fontTime")
b = Button(root,text="Record",command=rec,state=ACTIVE,bg="green",font="fontButton")
b1 = Button(root,text="Stop",command=stop,state=DISABLED,bg="red",font="fontButton")
b2 = Button(root, text = "Screenshot",command=screenshot,bg="orange",font="fontButton")
l = Label(root, text="")
l1 = Label(root, text="")
label.grid(row=0, column=0, columnspan=2)
b.grid(row=1, column=0, padx=1, pady=5)
b1.grid(row=1, column=1, padx=1)
b2.grid(row=1, column=2, padx=1)
l.grid(row=2, column=0,columnspan=2)
l1.grid(row=3, column=0,columnspan=2)
root.minsize(280,105)
root.maxsize(280,105)
root.title("Linux Screen Recorder")
root.attributes("-topmost", 1)
root.mainloop()
