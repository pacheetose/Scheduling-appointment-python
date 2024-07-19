import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
conn = sqlite3.connect('test2.db')
cursor = conn.execute("select date,p_name,doctor,department,time,number from sched1")
wind = tk.Tk();
wind.title("Admin Log-in")
wind.geometry("700x400")

img_path = "bg.jfif"
img = Image.open(img_path)
img1 = img.resize((700,400), resample=Image.LANCZOS)
background_image = ImageTk.PhotoImage(img)

label = tk.Label(wind, image=background_image)
label.place(relwidth=1, relheight=1)

def cancel():
    pass
def apsort():
    pass
def apsort1():
    pass

tree = ttk.Treeview(wind,selectmode='browse')
tree["columns"] =("1","2","3","4","5","6")
tree["show"] = 'headings'
tree.heading("1",text="date")
tree.heading("2",text="patient name")
tree.heading("3",text="doctor")
tree.heading("4",text="department")
tree.heading("5",text="time")
tree.heading("6",text="contact number")
tree.column("1",width=100,anchor='c')
tree.column("2",width=150,anchor='c')
tree.column("3",width=100,anchor='c')
tree.column("4",width=100,anchor='c')
tree.column("5",width=100,anchor='c')
tree.column("6",width=100,anchor='c')
for i in cursor:
    tree.insert(
    "",
    tk.END,
    values=(i[0],i[1],i[2],i[3],i[4],i[5])
)
button_frame = tk.Frame(wind)
cnc = tk.Button(button_frame,text="cancel appointment",command=cancel)
sort = tk.Button(button_frame,text="sort by department",command=apsort)
cnt = tk.Button(button_frame,text="doctor sched count",command=apsort1)
tree.pack()
cnc.pack(side=tk.LEFT)
sort.pack(side=tk.LEFT,padx=10)
cnt.pack(side=tk.RIGHT)
button_frame.pack(pady=20)

wind.mainloop()