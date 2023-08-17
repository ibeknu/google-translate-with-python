from tkinter import *
from tkinter import ttk,messagebox
#install dulu googletrans
import googletrans
from googletrans import Translator
import textblob




root = Tk()
root.title("Goolge Translator")
root.geometry("1080x400")

def label_change():
    c = combol.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

def translate_now():
    global language
    try:
        text_ = text1.get(1.0,END)
        c2= combol.get()
        c3= combo2.get()
        if(text_):
            words = textblob.TextBlob(text_)
            lan = words.detect_language()
            for i,j in language.items():
                if (j==c3):
                    lan_=i
            words = words.translate(from_lang=lan,to=str(lan_))
            text2.delete(1.0,END)
            text2.insert(END,words)
    except Exception as e:
        messagebox.showerror("googletranslate","please try again")

#icon
image_icon = PhotoImage(file="google transalte\google.png")
root.iconphoto(False,image_icon)

#arrrow
arrow_image = PhotoImage(file="google transalte\imagess.png")
image_label = Label(root,image=arrow_image,width=140)
image_label.place(x=460,y=50)

language = googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

#bahasa
combol = ttk.Combobox(root,values=languageV,font="Roboto 14", state="r")
combol.place(x=110,y=20)
combol.set("English")
label1 = Label(root,text="English", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10,y=50)

f = Frame(root,bg="Black", bd=5)
f.place(x=10,y=118,width=440,height=210)

text1 = Text(f, font="Roboto 20",bg="white",relief=GROOVE, wrap=WORD)
text1.place(x=0,y=0, width=430,height=200)

scroolbar1 = Scrollbar(f)
scroolbar1.pack(side="right", fill="y")

scroolbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scroolbar1.set)



#kanan
combo2 = ttk.Combobox(root,values=languageV,font="Robot 14",state="r")
combo2.place(x=730,y=20)
combo2.set("Select Lenguage")
label2 = Label(root,text="English", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620,y=50)
f1 = Frame(root,bg="Black", bd=5)
f1.place(x=620,y=118,width=440,height=210)

text2 = Text(f1, font="Roboto 20",bg="white",relief=GROOVE, wrap=WORD)
text2.place(x=0,y=0, width=430,height=200)

scroolbar2 = Scrollbar(f1)
scroolbar2.pack(side="right", fill="y")

scroolbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scroolbar2.set)




#trans button

translate = Button(root,text="Translate", font="Roboto 15 bold italic"
                   ,activebackground="purple", cursor="hand2", bd=5,bg="red", fg="white",command=translate_now)
translate.place(x=480,y=250)


label_change()

root.configure(bg="white")
root.mainloop()
