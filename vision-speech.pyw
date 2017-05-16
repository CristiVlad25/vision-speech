from tkinter import *
from tkinter import ttk
from threading import Thread
import pyvona
import urllib
import psutil
from PIL import Image
from keys import *
from watson_developer_cloud import VisualRecognitionV3 as vr

root = Tk()
root.resizable(0,0)
root.title('Image Recognizer')

label1 = ttk.Label(root, text="URL:")     
label1.grid(row=0, column=0)                
entry1 = ttk.Entry(root, width = 40)        
entry1.grid(row=0, column=1)

instance = vr(api_key=watson_key, version='2016-05-20')
v = pyvona.create_voice(key1, key2)
v.voice_name = 'Emma'

def callback():

    img = instance.classify(images_url=entry1.get())
    img1 = img['images'][0]['classifiers'][0]['classes'][0]
    img2 = Image.open(urllib.request.urlopen(entry1.get()))
    img2.show()
    entry1.delete(0, END)
    v.speak('\n There is a ' + str(int(img1['score']*100)) + ' percent chance you\'re looking at: '+ img1['class'])
    
    for things in img['images'][0]['classifiers'][0]['classes']:
        print('\n There is a ' + str(things['score']*100) + ' percent chance the image contains: '+ things['class'])

    for proc in psutil.process_iter():
        if proc.name() == "Microsoft.Photos.exe":
            proc.kill()
        
def thr():

    t1 = Thread(target=callback)
    t1.start()

button = Button(root, text='Recognize', command=thr, bd=0, overrelief='sunken')
button.grid(row=0, column=2)

entry1.focus()
root.mainloop()
