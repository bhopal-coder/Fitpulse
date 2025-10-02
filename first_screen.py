from tkinter import *
from PIL import Image, ImageTk
import userpanel
import trainerpanel
import adminlogin
class welcome:
    def __init__(self):
        self.root=Tk()
        self.root.title("Welcome Screen")
        self.width=self.root.winfo_screenwidth()-100
        self.height=self.root.winfo_screenheight()-100

        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False) 
        
        self.img_bg=Image.open('pastel orange3.jpg')
        self.img_bg_new=self.img_bg.resize((self.width,self.height))
        self.img_bg_tk=ImageTk.PhotoImage(self.img_bg_new)
        self.img_bg_label=Label(self.root,image=self.img_bg_tk)
        self.img_bg_label.place(x=0,y=0)

        self.img=Image.open('first screen.jpg')
        self.img_new=self.img.resize((550,550))
        self.img_new_tk=ImageTk.PhotoImage(self.img_new)
        self.img_label=Label(self.root,image=self.img_new_tk)
        self.img_label.place(x=590,y=33)

        self.frame1=Frame(self.root,bg="#150d66",width=567,height=553)
        self.frame1.place(x=36,y=33)


        self.img1=Image.open('logoproj-Photoroom.png')
        self.img1_new=self.img1.resize((164,115))
        self.img1_tk=ImageTk.PhotoImage(self.img1_new)
        self.img1_label=Label(self.root,image=self.img1_tk)
        self.img1_label.place(x=220,y=70)

        self.label=Label(self.root,text="CHOOSE YOUR ACCOUNT",font=('times new roman',15,'bold'),bg='#fcfffd',width=50)
        self.label.place(x=36,y=240)

        self.img4=Image.open('admin.jpg')
        self.img4_new=self.img4.resize((40,40))
        self.img4_new_tk=ImageTk.PhotoImage(self.img4_new)
        self.img4_label=Label(self.root,image=self.img4_new_tk)
        self.img4_label.place(x=170,y=300)
        
        self.but3=self.but1=Button(self.root,text="ADMIN PANEL",font=('times new roman',15,'bold'),height=1,bd=2, relief="solid",command=self.next_admin)
        self.but3.place(x=230,y=300)

        self.img2=Image.open('log user.jpg')
        self.img2_new=self.img2.resize((40,40))
        self.img2_new_tk=ImageTk.PhotoImage(self.img2_new)
        self.img2_label=Label(self.root,image=self.img2_new_tk)
        self.img2_label.place(x=170,y=360)

        self.but1=Button(self.root,text="USER PANEL",font=('times new roman',15,'bold'),height=1,bd=2, relief="solid",command=self.next_user)
        self.but1.place(x=230,y=360)

        self.img3=Image.open('logo trainer.jpg')
        self.img3_new=self.img3.resize((40,40))
        self.img3_tk=ImageTk.PhotoImage(self.img3_new)
        self.img3_label=Label(self.root,image=self.img3_tk)
        self.img3_label.place(x=170,y=420)

        self.but2=Button(self.root,text="TRAINER PANEL",font=('times new roman',15,'bold'),height=1,bd=2, relief="solid",command=self.next_trainer)
        self.but2.place(x=230,y=420)

        self.root.mainloop()
    def next_user(self):
        self.root.destroy()
        userpanel.user()

    def next_trainer(self):
        self.root.destroy()
        trainerpanel.trainer()
    def next_admin(self):
        self.root.destroy()
        adminlogin.login()


if __name__=="__main__":
     welcome()
   


 


        





       
