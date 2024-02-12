from tkinter import *
import pyshorteners

root=Tk()
root.title('URL Shortener')
root.configure(background='light blue')
p1=PhotoImage(file ="C:\\Users\\Sundar S\\Documents\\Python\\Projects\\URL Shortener\\URL_Shortener.png")
root.iconphoto(False, p1)
root.geometry("500x500")

def Shorten():
    if shorty_entry.get():
        shorty_entry.delete(0,END)

    if my_entry.get():
        #Convert to tiny url
        url=pyshorteners.Shortener().tinyurl.short(my_entry.get())
        #Output to Screen
        shorty_entry.insert(END,url)

        #Reverse URL
        print(pyshorteners.Shortener().tinyurl.expand(url))

def Clear_all():
    my_entry.delete(0,END)
    shorty_entry.delete(0,END)
    my_entry.focus_set()

my_lbl=Label(root,text="Enter the URL to Shorten:",font=("Times New Roman",25),bg='light blue')
my_lbl.pack(pady=20)

my_entry=Entry(root,font=("Times New Roman",24))
my_entry.pack(pady=20)

my_btn=Button(root,text="Shorten Link",command=Shorten,font=("Times New Roman",20),bg='violet')
my_btn.pack(pady=20)

shorty_lbl=Label(root,text="Shortened Link",font=("Times New Roman",24),bg='light blue')
shorty_lbl.pack(pady=30)

shorty_entry=Entry(root,font=("Times New Roman",22),justify=CENTER,width=30)
shorty_entry.pack(pady=10)

my_clr=Button(root,text="Clear All",command=Clear_all,font=("Times New Roman",20),bg='yellow')
my_clr.pack(pady=20)

root.mainloop()