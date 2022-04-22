import random
import re
import time
from tkinter import *
def to():
    global stg
    stg=time.time()

def too():
    global stg2
    stg2=time.time()-stg
    stg2=stg2/60

global c1
def wpma_pass(host, guest):  # this function takes two lists and compare every element of host with guest
    global length
    host=re.split("\s", host)
    guest=re.split("\s", guest)
    length=len(guest)
    print(host,guest,length)
    flag_1 = 0
    flag_2 = 0
    while True:
        for i in range(length):
            if guest[i] in host:
                flag_1 = flag_1 + 1
            if guest[i] not in host:
                flag_2 = flag_2 + 1
        return [flag_1, flag_2]
        break


t1 = "It is a long established fact that a reader will be distracted by the readable content of a page when "
t2 = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered "
t3 = "All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary,"
t4 = "encompasses the social behavior and norms found in human societies, as well as the knowledge"
t5 = "India is a country in South Asia whose name comes from the Indus River. The name 'Bharata' "
lista = [t1, t2, t3, t4, t5]
text = random.choice(lista)
def sub():
    too()
    username = entry.get()
    res=wpma_pass(text,username)
    strs="this is your"+" typing speed "+str(res[0]/stg2)
    win2=Tk()
    spe=Label(win2,text=strs,font=('calibre',10, 'bold')).pack()
    acc=Label(win2,text="your accuracy was "+str(res[0]/length*100),font=('calibre',10, 'bold')).pack()
    accc = Label(win2, text="thank you", font=('calibre', 10, 'bold')).pack()
    win2.mainloop()

def exit():
    win.quit()
win = Tk()
def clicked():
    to()
    global entry
    lab=Label(win,text=text,font=('calibre',20)).pack(side=TOP)
    entry = Entry(win,
                  font=("Arial",40),
                  fg="#00FF00",
                  bg="black")

    entry.pack()

l= Label(win,text="this is typing speed meter").pack()
b=Button(win,text="       start      ",
         command=clicked,
         fg="#55edb5",bg="#e34bfa").pack()

b3=Button(win,
          text="      exit      ",
          command=exit,fg="#55edb5",
          bg="#e34bfa").pack(side=RIGHT)
sumb=Button(win,text="      submit      ",command=sub,fg="#55edb5",bg="#e34bfa").pack(side=RIGHT)
win.mainloop()