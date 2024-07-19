import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
def go():
    win.destroy()
    import qui1
def ad():
    win.destroy()
    import adminLog
win = tk.Tk()
win.geometry("500x200")
win.title("Log in")

img_path = "background_img.jfif"
img = Image.open(img_path)
img1 = img.resize((500,300), resample=Image.LANCZOS)
background_image = ImageTk.PhotoImage(img)

label = tk.Label(win, image=background_image)
label.place(relwidth=1, relheight=1)

logLabel = tk.Label(master=win,text="Log in as: ",font="Calibri 24 bold")
logFrame = tk.Frame(master=win)
gbutton = tk.Button(master=logFrame,text="guest",font="calibri 15",command=go)
adbutton = tk.Button(master=logFrame,text="admin",font="calibri 15",command=ad)
logLabel.pack()
logFrame.pack(pady=35)
gbutton.pack(side=tk.LEFT,padx=10)
adbutton.pack(padx=10)
win.mainloop()
