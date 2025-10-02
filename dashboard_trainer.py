from tkinter import *
from PIL import Image,ImageTk
import trainerlogin
import database
import dash_trainer_details
import view_my_clients
class trainerboard:
    def __init__(self,res):
        self.root=Tk()
        self.root.title("Dashboard for trainer")
        self.res=res
        self.trainer_id = res[0] 
        self.width=self.root.winfo_screenwidth()-100
        self.height=self.root.winfo_screenheight()-100
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)
        
        self.image=Image.open('pastel orange3.jpg')
        self.image_new=self.image.resize((self.width,self.height))
        self.image_new_tk=ImageTk.PhotoImage(self.image_new)
        self.image_label=Label(self.root,image=self.image_new_tk)
        self.image_label.place(x=0,y=0)

        self.image1=Image.open('dashboard trainer.jpg')
        self.image1_new=self.image1.resize((1140,580))
        self.image1_new_tk=ImageTk.PhotoImage(self.image1_new)
        self.image1_label=Label(self.root,image=self.image1_new_tk)
        self.image1_label.place(x=20,y=20) 
 

        self.frame1=Frame(self.root,bg="#ebe4f5",width=1144,height=190)  
        self.frame1.place(x=20,y=20) 

        self.frame3=Frame(self.root,bg="#ebe4f5",width=590,height=583)
        self.frame3.place(x=20,y=20)


        self.frame2=Frame(self.root,bg="#093887",width=1145,height=100)
        self.frame2.place(x=20,y=20) 

        self.but1=Button(self.root,text=('Personal info'), font=('times new roman',15,'bold'),bg="#093887",fg="#ebe4f5",bd=0,command=self.nextscreen)
        self.but1.place(x=160,y=63)

        self.but2=Button(self.root,text=('Client Details'), font=('times new roman',15,'bold'),bg="#093887",fg="#ebe4f5",bd=0, command=self.allClients)
        self.but2.place(x=310,y=63)

        

        self.but6=Button(self.root,text=('LogOut'), font=('times new roman',15,'bold'),bg="#093887",fg="#ebe4f5",bd=1,command=self.logout)
        self.but6.place(x=1070,y=63)

        self.image2=Image.open('logoproj-Photoroom.png')
        self.image2_new=self.image2.resize((100,100))
        self.image2_new_tk=ImageTk.PhotoImage(self.image2_new)
        self.image2_label=Label(self.root,image=self.image2_new_tk)
        self.image2_label.place(x=20,y=20) 

        self.labelquote=Label(self.root,text="Every client's journey stands as a testament :",bg="#ebe4f5",font=('times new roaman',14,'bold'))
        self.labelquote.place(x=80,y=300)

        self.labelqoute1=Label(self.root,text="Great Trainers not only shape bodies but also",bg="#ebe4f5",font=('times new roman',16,'bold'))
        self.labelqoute1.place(x=80,y=330)

        self.labelqoute1=Label(self.root,text="profoundly impact lives , forging lasting ",bg="#ebe4f5",font=('times new roman',16,'bold'))
        self.labelqoute1.place(x=80,y=360)

        self.labelqoute1=Label(self.root,text="Transformations",bg="#ebe4f5",font=('times new roman',16,'bold'))
        self.labelqoute1.place(x=80,y=390)

        self.root.mainloop()
    def logout(self):
        self.root.destroy()
        trainerlogin.login()
    def allClients(self):
        self.root.destroy()
        view_my_clients.ViewMyClients(self.trainer_id,self.res)
        
    def nextscreen(self):
        self.root.destroy()
        dash_trainer_details.details(self.res)

if __name__=="__main__":
    trainerboard()