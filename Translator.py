from tkinter import *
from textblob import TextBlob as tb
import pyttsx3

#pilih bahasa#
def IND(): #ID 
   t2.delete('1.0',END)
   t = t1.get("1.0",'end-1c')
   s = tb(t) 
   tr = s.translate(from_lang=s.detect_language(),to='id')
   t2.insert(END,tr)

def ENG(): #EN 
   t2.delete('1.0',END)
   t = t1.get("1.0",'end-1c')
   s = tb(t)
   tr = s.translate(from_lang=s.detect_language(),to='en')
   t2.insert(END,tr)

def ReadEN(): #ReadInEn
	t = t2.get("1.0",'end-1c')
	s = tb(t)
	tts = pyttsx3.init()
	tts.say(s)
	tts.runAndWait()

def ARB(): #AR
   t2.delete('1.0',END)
   t = t1.get("1.0",'end-1c')
   s = tb(t) 
   tr = s.translate(from_lang=s.detect_language(),to='ar')
   t2.insert(END,tr)

def JAP(): #JA 
   t2.delete('1.0',END)
   t = t1.get("1.0",'end-1c')
   s = tb(t) 
   tr = s.translate(from_lang=s.detect_language(),to='ja')
   t2.insert(END,tr)

def GER(): #DE 
   t2.delete('1.0',END)
   t = t1.get("1.0",'end-1c')
   s = tb(t) 
   tr = s.translate(from_lang=s.detect_language(),to='de')
   t2.insert(END,tr)
# #

#reset IO#
def res():
	t1.delete('1.0',END)
	t2.delete('1.0',END)
# #

#tampilan#

#win#
master = Tk()

#input#
Label(master, text="Teks yang ingin Anda terjemahkan", font=('Calibri',14,'bold')).grid(row=0,column=0,padx=4)
t1 = Text(master,width=100,height=20)
t1.grid(row=1, column=0, padx=4)

#output#
Label(master, text="Hasil terjemahan", font=('Calibri',14,'bold')).grid(row=2,column=0,padx=4)
t2 = Text(master,width=100,height=20)
t2.grid(row=3, column=0, padx=4)

#opsi#
Button(master, text='ID', font=('Arial',10,'bold'), command=IND).grid(row=4, column=0, sticky=W, padx=4, pady=4, columnspan=2)
Button(master, text='EN', font=('Arial',10,'bold'), command=ENG).grid(row=4, column=0, sticky=W, padx=40, pady=4, columnspan=2)
Button(master, text='AR', font=('Arial',10,'bold'), command=ARB).grid(row=4, column=0, sticky=W, padx=80, pady=4, columnspan=2)
Button(master, text='JA', font=('Arial',10,'bold'), command=JAP).grid(row=4, column=0, sticky=W, padx=120, pady=4, columnspan=2)
Button(master, text='DE', font=('Arial',10,'bold'), command=GER).grid(row=4, column=0, sticky=W, padx=160, pady=4, columnspan=2)

#utilitas#
Button(master, text='Baca', font=('Arial',12,'bold'), command=ReadEN).grid(row=4, column=0, sticky=W, padx=220, pady=4)
Button(master, text='Hapus', font=('Arial',12,'bold'), command=res).grid(row=4, column=0, sticky=W, padx=280, pady=4)
Button(master, text='Keluar', font=('Arial',12,'bold'), command=master.quit).grid(row=4, column=0, sticky=W, padx=350,pady=4)
# #

master.mainloop()