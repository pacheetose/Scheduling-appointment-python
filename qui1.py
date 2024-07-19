import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
import time
conn = sqlite3.connect('test2.db')
cutime = [time.localtime().tm_mon,time.localtime().tm_mday,time.localtime().tm_year]
tm = "{}-{}-{}".format(cutime[0],cutime[1],cutime[2])
window = tk.Tk()
window.geometry('700x400')
window.title('ChatBot.io')


img_path = "background_img.jfif"
img = Image.open(img_path)
img1 = img.resize((700,400), resample=Image.LANCZOS)
background_image = ImageTk.PhotoImage(img)

label = tk.Label(image=background_image)
label.place(relwidth=1, relheight=1)

dep_info = []
faqli=['How can I make an appointment with a doctor?',
'What documents do I need to bring for my appointment?',
'What are the visiting hours for patients?',
'What are the payment options for medical services?',
'How long will I have to wait for my test results?',
'What should I do if I need to cancel or reschedule my appointment?',
'Are there any restrictions on food or drink before a procedure?',
'What should I do if I have an emergency outside of regular hospital hours?',
'What are the visiting policies for patients in the hospital?',
'Can I have someone accompany me during my hospital stay or procedure?',
'How do I obtain my medical records or request a copy of my test results?',
'Can I get a second opinion from another doctor within the hospital?',
'What insurance plans do you accept, and how does billing work?',
'Are there any support groups or resources available for patients and their families?',
'What should I expect during my hospital stay or surgical procedure?',
'Are there any special instructions for preparing for a specific medical test or procedure?',
'What are the potential risks and complications of the recommended treatment?',
'Will I need any follow-up appointments or ongoing care after my treatment?',
'How can I reach my doctor or the hospital for non-emergency questions or concerns?',
"Can you provide information about the hospital's infection control measures?"]
response = {'hi':'hello','hello':'hi',
            'hospital rates':"Our rates varies per department or procedures included\nto your consultation.For further details contact our \ninfomation desk. Thank you!",
            "make an appointment": "Choose a department based on your symptoms\n Press help to see what each department covers\nPress the 'Set Appointment' Button Below.\nFill in your name and choose the doctor and schedule.",
            'how can i make an appointment with a doctor?':"Choose a department based on your symptoms\n Press help to see what each department covers\nPress the 'Set Appointment' Button Below.\nFill in your name and choose the doctor and schedule.",
            "visiting hours":"7 am to 11 am in the morning\n1:00 pm to 5:00 pm\nAll hours for emergency cases",
            'what are the visiting hours for patients?':"7 am to 11 am in the morning\n1:00 pm to 5:00 pm\nAll hours for emergency cases",
            "how long will i have to wait for my test results?":"Routine blood tests and urine tests: A few hours-a few days\nX-ray/CT Scan/MRI: a few days (interpretation required)\nOthers (more complex tests): a week or more",
            "test results":"Routine blood tests and urine tests: A few hours-a few days\nX-ray/CT Scan/MRI: a few days (interpretation required)\nOthers (more complex tests): a week or more",
            "what should i do if i need to cancel or reschedule my appointment?":"Contact our information desk to redirect you to\n the department you are currently scheduled on.\n The department representative will then give you the new date\n based on availability or the process for cancellation.",
            "cancel appointment":"Contact our information desk to redirect you to the \ndepartment you are currently scheduled on. The department \nrepresentative will then give you theprocess for cancellation.",
            "reschedule appointment":"Contact our information desk to redirect you to the department\n you are currently scheduled on. The department representative \nwill then give you the new date based on availability.",
            "Are there any restrictions on food or drink before a procedure?":"Food restrictions before a medical procedure can vary \ndepending on the procedure. These will be given to you \ndays before the operation. You should follow it as these \n will minimize the risk of complications during the procedure.",
            "food restrictions":"Food restrictions before a medical procedure can vary \ndepending on the procedure. These will be given to you \ndays before the operation. You should follow it as these \n will minimize the risk of complications during the procedure.",
            "food and drinks":"The hospital has a local canteen with a variety\n of choices if you are hungry waiting",
            'food':"The hospital has a local canteen with a variety\n of choices if you are hungry waiting",
            'drinks':"We have various stalls offering drinks, as well \n as vending machines and water on our local canteen",
            "restrictions":"Aside from food restrictions before procedures we alsohave \nvarious other restrictions posted on every corner of the \nestablishment such as hygiene and smoking restrictions",
            'what should i do if i have an emergency outside of regular hospital hours?':"Our hospital is open 24 hours for emergency cases",
            'emergency':"Our hospital is open 24 hours for emergency cases",
            "what are the visiting policies for patients in the hospital?":"Unlicensed weapons are prohibited inside the hospital\nSmoking are only allowed to some open areas within. We\n recommend still using face mask and sanitizers to avoid transmission",
            "policies":"Unlicensed weapons are prohibited inside the hospital.Smoking\nare only allowed to some open areas within. We recommend \nstill using face mask and sanitizers to avoid transmission",
            "rules":"Unlicensed weapons are prohibited inside the hospital\nSmoking are only allowed to some open areas within. We\n recommend still using face mask and sanitizers to avoid transmission\nAlso see: hospital policy",
            "security policies":"Unlicensed weapons are prohibited inside the hospital\nSmoking are only allowed to some open areas within. We\n recommend still using face mask and sanitizers to avoid transmission\n Also see: hospital policy",
            "hospital policy":"We have a first come, first serve policy, except for\n emergency life and death cases that should be prioritized.\n Patients with appointment will also be prioritized.\nAlso see: security policies.",
            "policy":"We have a first come, first serve policy, except for\n emergency life and death cases that should be prioritized.\n Patients with appointment will also be prioritized.\nAlso see: security policies.",
            "can i have someone accompany me during my hospital stay or procedure?":"Patient companions will have to stay at the waiting area\n during procedures. They have to follow visiting hours otherwise.",
            "companion":"Patient companions will have to stay at the waiting area\n during procedures. They have to follow visiting hours otherwise.",
            "how do i obtain my medical records or request a copy of my test results?":"Go to the medical records department with the following:\n - Valid ID\n- Proof of payment",
            "record":"Go to the medical records department with the following:\n - Valid ID\n- Proof of payment",
            "medical record":"Go to the medical records department with the following:\n - Valid ID\n- Proof of payment",
            "request":"request what?",
            "request record":"Go to the medical records department with the following:\n - Valid ID\n- Proof of payment",
            "request medical record":"Go to the medical records department with the following:\n - Valid ID\n- Proof of payment",
            "what insurance plans do you accept, and how does billing work?":"We accept any type of health insurance which may cover\n your full bill depending on you insurance plan.\nYour bill will be issued and should be paid before \n any procedure. We accept later payment with a promisory note.",
            "insurance":"We accept any type of health insurance which may cover\n your full bill depending on you insurance plan.\nYour bill will be issued and should be paid before  any\n procedure. We accept later payment with a promisory note",
            "philhealth":"The case rate amount shall be deducted by the health care \ninstitution from the member’s total bill, which shall include \nprofessional fees of attending physicians, prior to discharge.\n For other cases, visit the neares PhilHealth office for details",
            "hmo":"Please visit our home website to see our accredited companies",
            'health card':'Please visit our home website to see our accredited companies',
            "billing":"We accept any type of health insurance which may cover\n your full bill depending on you insurance plan.\nYour bill will be issued and should be paid before \n any procedure. We accept later payment with a promisory note",
            "are there any support groups or resources available for patients and their families?":"Right now, we have no support groups inside the facility.",
            "support groups":"Right now, we have no support groups inside the facility.",
            "what should i expect during my hospital stay or surgical procedure?":"It's important to note that every hospital stay can be \nunique, depending on the patient's condition, the nature of\n their treatment, and the specific policies and practices of the \nhospital. Patients are encouraged to communicate with their \nhealthcare team, ask questions, and actively participate in their\n care to ensure a positive hospital experience.",
            "hospital stay":"It's important to note that every hospital stay can be \nunique, depending on the patient's condition, the nature of\n their treatment, and the specific policies and practices of the \nhospital. Patients are encouraged to communicate with their \nhealthcare team, ask questions, and actively participate in their\n care to ensure a positive hospital experience.",
            "surgery":"It's important to note that every hospital stay can be \nunique, depending on the patient's condition, the nature of\n their treatment, and the specific policies and practices of the \nhospital. Patients are encouraged to communicate with their \nhealthcare team, ask questions, and actively participate in their \ncare to ensure a positive hospital experience.",
            "are there any special instructions for preparing for a specific medical test or procedure?":"Special instructions will be given by your doctor after check up",
            "what are the potential risks and complications of the recommended treatment?":"Risks can vary from internal infections, swelling, etc.\n This may occur if your failed to follow procedures.\n Otherwise please file a complain to our info desk for investigation",
            "will i need any follow-up appointments or ongoing care after my treatment?":"We don't require follow-up check ups, unless it was instructed\n by your physician or if symptoms still occur.",
            "follow-up":"We don't require follow-up check ups, unless it was instructed\n by your physician or if symptoms still occur.",
            "follow up":"We don't require follow-up check ups, unless it was instructed\n by your physician or if symptoms still occur.",
            "how can i reach my doctor or the hospital for non-emergency questions or concerns?":"Contact our info desk (number at the help button).\n They will give you contact information of your assigned doctor",
            "questions":"Contact our info desk (see number by pressing help button)",
            "inquiry":"Contact our info desk (see number by pressing help button)",
            "hospital contact":"Press help button to see our contact info",
            "hospital address":"Press help button to see our contact info",
            "address":"Press help button to see our contact info",
            "can you provide information about the hospital's infection control measures?":"Our hospital have various infection precautions.\nThis include but not limited to:\nHygiene protocols, PPEs, Environmental cleaning, Disinfection",
            "":"--__--",
            "cardiology": "the branch of medicine that focuses on the diagnosis,\n treatment, and prevention of diseases and conditions related \nto the heart and blood vessels.",
            "pediatrics":" a branch of medicine that focuses on the medical care and \n well-being of infants, children, and adolescents.",
            "orthopedics":"a medical specialty focused on the diagnosis, treatment, and \nprevention of conditions and injuries related to the musculoskeletal \nsystem. This includes bones, joints, muscles, tendons, ligaments,\n and other structures that support and enable movement.",
            "ophthalmology": "a branch of medicine that deals with the diagnosis, treatment, \nand prevention of eye-related conditions and diseases.",
            "geriatrics":"a branch of medicine that specializes in the healthcare of older \nadults, typically aged 65 and older.",
            "neurology":"a branch of medicine that deals with the diagnosis and treatment of \nconditions affecting the nervous system, which includes the brain,\n spinal cord, and peripheral nerves.",
            "dermatology":"branch of medicine that deals with the study, diagnosis & treatment\n of conditions affecting the skin, hair, nails, and related structures.",
            "urology":"branch of medicine that deals with the study, diagnosis & treatment\n of conditions affecting the urinary system, which includes the kidneys,\n bladder, ureters, and urethra, as well as the male reproductive\n system, including the prostate, testes, and penis.",
            "obgyn": "obstetrics and gynecologyis a branch of medicine that deals with the care\n of women's reproductive health, including pregnancy, childbirth, and \nvarious conditions related to the female reproductive system.",
            "gastroenterology":"branch of medicine that deals with the study, diagnosis & treatment\n of conditions affecting the digestive system, which includes the\n esophagus, stomach, intestines, liver, gallbladder, and pancreas."
                        }
dept = ['Cardiology','Pediatrics','Orthopedics','Ophthalmology','Geriatric','Neurology','Dermatology','Urology','OBGYN','Gastroenterology']
dc = { 'Cardiology' : ["Dr. Velasquez","Dr. Beltran","Dr. Dominguez"],
'Pediatrics' : ["Dr. Herbert","Dr. Silva","Dr. Zaragoza"],
'Orthopedics' : ["Dr. Cruz","Dr. Santos","Dr. Lee"],
'Ophthalmology' : ["Dr. Navaro","Dr. Gonzales","Dr. Aquino"],
'Geriatric' : ["Dr. Fernandez","Dr. Del Rosario","Dr. Salvador"],
'Neurology' : ["Dr. Castro","Dr. Salazar","Dr. Alcantara"],
'Dermatology' : ["Dr. Ma","Dr. Lee","Dr. Lim"],
'Urology' : ["Dr. Flores","Dr. Villanueva","Dr. Rivera"],
'OBGYN' : ["Dr. Ramirez","Dr. Chong","Dr. Castillo"],
'Gastroenterology' : ["Dr. Dizon","Dr. Dela Cruz","Dr. Lim"]}

sch=["Please choose your schedule: ","7:00-9:00","9:00-11:00","13:00-15:00","15:00-17:00"]
def send():
    ui=ent_val.get()
    ui.strip()
    if response.get(ui)!=None:
        outp.set(response.get(ui))
        ent_val.set('')
    else:
        outp.set("Invalid input")
        ent_val.set('')


def key_down(e):
    send()
def win():
    def conf():
        mxx=0
        mx = conn.execute("select max(id) from sched1")
        for i in mx:
            print(i)
            if i[0]==None:
                mxx=1
            else:
                mxx=i[0]+1

        ni = str(combi.get())
        sc = str(combi2.get())
        if str(nm.get())=="" or str(nm2.get())=="" or ni=="Select a doctor from the department: " or sc=="Please choose your schedule: ":
            errortxt.set("insufficient input")
        else:
            c = conn.cursor()
            c.execute("insert into sched1 values (:date,:p_name,:doctor,:department,:time,:number,:id)",
                         {
                             'date':tm,
                             'p_name':nm.get()+" "+nm2.get(),
                             'doctor':combi.get(),
                             'department':dept_choice.get(),
                             'time':combi2.get(),
                             'number':nm3.get(),
                             'id':mxx
                         })
            conn.commit()
            combi.configure(state="disabled")
            wind.destroy()
    if dept_choice.get() == "Choose department":
        outp.set("Specify department to set appointment")
    else:
        choice=dc[dept_choice.get()]
        wind = tk.Tk()
        wind.geometry('300x200')
        ff = tk.Frame(wind)
        ff2 = tk.Frame(wind)
        ff3 = tk.Frame(wind)
        nlab = tk.Label(master=ff,text="Patient firstname: ")
        nm = tk.Entry(master=ff)
        nlab2 = tk.Label(master=ff2, text="Patient lastname: ")
        nm2 = tk.Entry(master=ff2)
        nlab3 = tk.Label(master=ff3, text="contact number: ")
        nm3 = tk.Entry(master=ff3)
        combi = ttk.Combobox(wind,values=choice)
        combi.set("Select a doctor from the department: ")
        combi2 = ttk.Combobox(wind, values=sch)
        combi2.current(0)
        cb = tk.Button(wind,text="confirm",command=conf)
        errortxt = tk.StringVar()
        error = tk.Label(wind,textvariable=errortxt)
        ff.pack()
        ff2.pack()
        ff3.pack()
        nlab.pack(side=tk.LEFT)
        nm.pack(side=tk.RIGHT)
        nlab2.pack(side=tk.LEFT)
        nm2.pack(side=tk.RIGHT)
        nlab3.pack(side=tk.LEFT)
        nm3.pack(side=tk.RIGHT)
        combi.pack()
        combi2.pack()
        cb.pack()
        error.pack()
        wind.mainloop()
def exi():
    window.destroy()
def hlp():
    help_window = tk.Tk()
    help_window.title('help')
    help_window.geometry('500x200')
    help_lab1 = tk.Label(help_window,text="Contact us: ",font="Calibri 20 bold",)
    help_lab2 = tk.Label(help_window,text="Info desk: 202-918-2132 \nComplain desk: 321-401-6760",font="Calibri 10",padx=15)
    help_lab3 = tk.Label(help_window, text="Visit us: ", font="Calibri 20 bold",)
    help_lab4 = tk.Label(help_window, text="Address:  1227 A. Mabini corner Padre Faura Streets, 1000", font="Calibri 10",
                         padx=15)
    help_lab5 = tk.Label(help_window,text="*If you are confused to department choices, type in\n the department name in the chat bot to see their coverage*",font="Calibri 10",pady= 10)
    help_lab1.pack()
    help_lab2.pack()
    help_lab3.pack()
    help_lab4.pack()
    help_lab5.pack()
    help_window.mainloop()
def faqc():
    faq_window = tk.Tk()
    faq_window.geometry('650x500')
    faq_window.title("User Guide Questions")
    faq_top = tk.Label(faq_window,text="Frequently asked Questions: ",font="Calibri 20 bold")
#    faq_label=tk.Label(faq_window,justify=tk.LEFT,font="Calibri 12",text="* How can I make an appointment with a doctor?\n* What documents do I need to bring for my appointment?\n* What are the visiting hours for patients?\n* What are the payment options for medical services?\n* How long will I have to wait for my test results?\n* What should I do if I need to cancel or reschedule my appointment?\n* Are there any restrictions on food or drink before a procedure?\n* What should I do if I have an emergency outside of regular hospital hours?\n* What are the visiting policies for patients in the hospital?\n* Can I have someone accompany me during my hospital stay or procedure?\n* How do I obtain my medical records or request a copy of my test results?\n* Can I get a second opinion from another doctor within the hospital?\n* What insurance plans do you accept, and how does billing work?\n* Are there any support groups or resources available for patients and their families?\n* What should I expect during my hospital stay or surgical procedure?\n* Are there any special instructions for preparing for a specific medical test or procedure?\n* What are the potential risks and complications of the recommended treatment?\n* Will I need any follow-up appointments or ongoing care after my treatment?\n* How can I reach my doctor or the hospital for non-emergency questions or concerns?\n* Can you provide information about the hospital's infection control measures?")
    faq_list=tk.Listbox(faq_window,width=100,height=21,font="calibri 12")
    for i in range(len(faqli)):
        faq_list.insert(i+1,"* "+faqli[i])
    faq_top.pack(pady=10)
#    faq_label.pack(pady=15)
    faq_list.pack()
    faq_window.mainloop()
lab=tk.Label(master=window,text="How can I help you?",font="Calibri 24")
fr=tk.Frame(master=window)
ent_val=tk.StringVar()
ent=tk.Entry(master=fr,font="Calibri 20",textvariable=ent_val)
snd=tk.Button(master=fr,text="Send",font="Calibri 15",command=send)
outp = tk.StringVar()
outlab=tk.Label(master=window,font="Calibri 15",textvariable=outp)
dept_choice = ttk.Combobox(window,values=dept,state="readonly")
dept_choice.set("Choose department")
fr2 = tk.Frame(master=window)
hp = tk.Button(master=fr2,text="help",command=hlp)
faq = tk.Button(master=fr2,text="FAQ",command=faqc)
ne = tk.Button(master=fr2,text="Set Appointment",command=win)
ex = tk.Button(master=fr2,text="exit",command=exi)
ent.bind("<Return>",key_down)
lab.pack()
fr.pack()
ent.pack(side="left")
snd.pack(side="left")
outlab.pack(ipady=15)
dept_choice.pack(pady=(0,5))
fr2.pack(pady=10)
faq.pack(side=tk.LEFT,padx=10)
hp.pack(side=tk.LEFT)
ne.pack(padx=10,side=tk.LEFT)
ex.pack(side=tk.RIGHT)
window.mainloop()