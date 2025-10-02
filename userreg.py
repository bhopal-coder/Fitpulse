from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
class register:
    def __init__(self):
        self.root=Tk()
        self.root.title("Register Screen")
        self.width=self.root.winfo_screenwidth()-100
        self.height=self.root.winfo_screenheight()-100

        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)

        self.img_bg=Image.open('background1.jpg')
        self.img_bg_new=self.img_bg.resize((self.width,self.height))
        self.img_bg_tk=ImageTk.PhotoImage(self.img_bg_new)
        self.img_bg_label=Label(self.root,image=self.img_bg_tk)
        self.img_bg_label.place(x=0,y=0)
        
        
        self.img=Image.open('imagereg.jpg')
        self.img_new=self.img.resize((590,580))
        self.img_tk=ImageTk.PhotoImage(self.img_new)
        self.img_label=Label(self.root,image=self.img_tk)
        self.img_label.place(x=25,y=20)

        self.frame=Frame(self.root,background="#eb818a",width=567,height=583)
        self.frame.place(x=590,y=20)
        self.frame1=Frame(self.root,background="#fcfffd",width=450,height=495)
        self.frame1.place(x=650,y=60)

    
    
        self.img1=Image.open('logoproj-Photoroom.png')
        self.img1_new=self.img1.resize((350,120))
        self.img1_tk=ImageTk.PhotoImage(self.img1_new)
        self.img1_label=Label(self.root,image=self.img1_tk)
        self.img1_label.place(x=700,y=80)

        
        self.label=Label(self.root,text="NAME",bg="#fcfffd",font=('times new roman',15,'bold'))
        self.label.place(x=690,y=250)
        self.name_box=Entry(self.root,font=('times new roman',15,'bold'),background="#a5b6f2")
        self.name_box.place(x=830,y=250)
        self.label1=Label(self.root,text="EMAIL",bg="#fcfffd",font=('times new roman',15,'bold'))
        self.label1.place(x=690,y=290)
        self.email_box=Entry(self.root,font=('times new roman',15,'bold'),background="#a5b6f2")
        self.email_box.place(x=830,y=290)
        self.label2=Label(self.root,text="PASSWORD",bg="#fcfffd",font=('times new roman',15,'bold'))
        self.label2.place(x=690,y=330)
        self.password_box=Entry(self.root,font=('times new roman',15,'bold'),background="#a5b6f2")
        self.password_box.place(x=830,y=330)

        self.button1=Button(self.root,text="REGISTER",font=('times new roman',15,'bold'),bg="#eb818a", bd=2, relief="solid")
        self.button1.place(x=945,y=370)

        self.label_acc=Label(self.root,text="Already have an account?",font=('times new roman',15,'bold'),background="#fcfffd")
        self.label_acc.place(x=690,y=470)
        self.button2=Button(self.root,text="LOG IN",font=("times new roman",15,'bold'),bg="#eb818a", bd=2, relief="solid")      
        self.button2.place(x=945,y=470)

        
       
      
      

        



        

    

        self.root.mainloop()
obj=register()