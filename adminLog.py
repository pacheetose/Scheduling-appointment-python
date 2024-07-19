
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

conn = sqlite3.connect('test2.db')
wind = tk.Tk()
wind.title("Admin Log-in")
wind.geometry("500x300")


img_path = "background_img.jfif"
img = Image.open(img_path)
img1 = img.resize((500,300), resample=Image.LANCZOS)
background_image = ImageTk.PhotoImage(img)

label = tk.Label(wind, image=background_image)
label.place(relwidth=1, relheight=1)

def check():
    passw = str(passtxt.get())
    uname = str(nametxt.get())
    cursor = conn.execute("select uname, password from admin")
    print("{} {}".format(uname,passw))
    for i in cursor:
        if uname == i[0] and passw == i[1]:
            wind.destroy()
            import AdminPage

    print(cursor.rowcount)
mainLab = tk.Label(master=wind,text="Admin Sign in: ",font="Calibri 25 bold")
inframe = tk.Frame(master=wind)
namefr = tk.Frame(master=inframe)
nameLab = tk.Label(master=namefr,text="Username: ",font='Calibri 12')
nametxt = tk.Entry(master=namefr,font='Calibri 12')
passfr = tk.Frame(master=inframe)
passLab = tk.Label(master=passfr,text="Password: ",font='Calibri 12')
passtxt = tk.Entry(master=passfr,font='Calibri 12')
passtxt.config(show="*")
goButton = tk.Button(master=wind,text="Log-in",command=check)

mainLab.pack()
inframe.pack(pady=25)
namefr.pack()
nameLab.pack(side=tk.LEFT)
nametxt.pack()
passfr.pack()
passLab.pack(side=tk.LEFT)
passtxt.pack()
goButton.pack()
wind.mainloop()