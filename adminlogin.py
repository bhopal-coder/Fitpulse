from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import trainerpanel
import database 
import admin_dashboard
import dashboard_trainer

class login:
    def __init__(self):
        self.root=Tk()
        self.root.title("Login Screen For Admin")
        self.root.geometry('1150x600')
        self.root.resizable(False,False)

        self.img_bg=Image.open('pastel orange3.jpg')
        self.img_bg_new=self.img_bg.resize((1150,600))
        self.img_bg_tk=ImageTk.PhotoImage(self.img_bg_new)
        self.img_bg_label=Label(self.root,image=self.img_bg_tk)
        self.img_bg_label.place(x=0,y=0)
        
        
        self.img=Image.open('trainer1.jpg')
        self.img_new=self.img.resize((660,550))
        self.img_tk=ImageTk.PhotoImage(self.img_new)
        self.img_label=Label(self.root,image=self.img_tk)
        self.img_label.place(x=48,y=36)

        self.frame=Frame(self.root,background="#318CE7",width=570,height=553)
        self.frame.place(x=550,y=36)
        # self.frame1=Frame(self.root,background="#fcfffd",width=600,height=560)
        # self.frame1.place(x=710,y=80)

        self.logo=Image.open('login icon.jpg')
        self.logo_new=self.logo.resize((140,140))
        self.logo_tk=ImageTk.PhotoImage(self.logo_new)
        self.logo_label=Label(self.root,image=self.logo_tk)
        self.logo_label.place(x=755,y=70)


        self.label1=Label(self.root,text="EMAIL",bg="#318CE7",font=('times new roman',17,'bold'),fg="#fcfffd")
        self.label1.place(x=600,y=290)
        self.email_box=Entry(self.root,font=('times new roman',15,'bold'),background="#fcfffd")
        self.email_box.place(x=750,y=290)
        
        self.label2=Label(self.root,text="PASSWORD",bg="#318CE7",font=('times new roman',17,'bold'),fg="#fcfffd")
        self.label2.place(x=600,y=350)
        self.password_box=Entry(self.root,font=('times new roman',15,'bold'),background="#fcfffd")
        self.password_box.place(x=750,y=350)

        self.button1=Button(self.root,text="LOGIN",font=('times new roman',15,'bold'),bg="#fcfffd", bd=2, relief="solid",command=self.trainer)
        self.button1.place(x=820,y=400)

        self.root.mainloop()


    
    def back(self):
        pass
    #    self.root.destroy()
    #    trainerpanel.trainer()


    def trainer(self):
        data=(self.email_box.get() ,self.password_box.get())
        # print(data)
        
        res= database.loginAdmin(data)
        print(res)
        if res:
            
            messagebox.showinfo("Success","Admin Login Successfully")
            self.root.destroy()
            admin_dashboard.home_screen()
        else:
            messagebox.showerror("Error","User not exist")




        
if __name__=="__main__":
    login()

