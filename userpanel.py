from tkinter import *
from PIL import Image,ImageTk
import userlogin
import first_screen
import user_register
class user:
    def __init__(self):
        self.root=Tk()
        self.root.title('User Panel ')
        self.width=self.root.winfo_screenwidth()-100
        self.height=self.root.winfo_screenheight()-100

        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)

        self.img_bg=Image.open('pastel orange3.jpg')
        self.img_bg_new=self.img_bg.resize((self.width,self.height))
        self.img_bg_tk=ImageTk.PhotoImage(self.img_bg_new)
        self.img_bg_label=Label(self.root,image=self.img_bg_tk)
        self.img_bg_label.place(x=0,y=0)

        self.img=Image.open('imagereg.jpg')
        self.img_new=self.img.resize((550,550))
        self.img_tk=ImageTk.PhotoImage(self.img_new)
        self.img_label=Label(self.root,image=self.img_tk)
        self.img_label.place(x=36,y=33)

        self.frame=Frame(self.root,background="#011F5B",width=555,height=552)# orange code""#FA8072#007FFF
        self.frame.place(x=590,y=33)

        
        self.img1=Image.open('log user.jpg')
        self.img1_new=self.img1.resize((130,130))
        self.img1_tk=ImageTk.PhotoImage(self.img1_new)
        self.img1_label=Label(self.root,image=self.img1_tk)
        self.img1_label.place(x=790,y=50)

        self.label=Label(self.root,text="HEY  USER  WELCOME  TO  FIT  PLUSE",font=('times new roman',16,'bold'),bg="#fcfffd",width=46,height=1)
        self.label.place(x=588,y=220)

        self.img2=Image.open('create account logo.png')
        self.img2_new=self.img2.resize((44,39))
        self.img2_tk=ImageTk.PhotoImage(self.img2_new)
        self.img2_label=Label(self.root,image=self.img2_tk)
        self.img2_label.place(x=625,y=340)

        self.but1=Button(self.root,text="CLICK  TO  CREATE  NEW  ACCOUNT",font=('times new roman',15,'bold'),height=1,bd=2, relief="solid",command=self.register)
        self.but1.place(x=695,y=340)
        

        self.img3=Image.open('login icon.jpg')
        self.img3_new=self.img3.resize((44,39))
        self.img3_tk=ImageTk.PhotoImage(self.img3_new)
        self.img3_label=Label(self.root,image=self.img3_tk)
        self.img3_label.place(x=625,y=420)

        self.but2=Button(self.root,text="CLICK  TO  LOGIN  INTO  YOUR  ACCOUNT",font=('times new roman',15,'bold'),height=1,bd=2, relief="solid",command=self.login)
        self.but2.place(x=695,y=420)

        self.imgback=Image.open('back.jpg')
        self.imgback_new=self.imgback.resize((30,30))
        self.imgback_tk=ImageTk.PhotoImage(self.imgback_new)
        self.back_button=Button(self.root, text="BACK",image=self.imgback_tk,command=self.back,bg="white",bd=2,relief="solid")
        self.back_button.place(x=0,y=0)

        
        self.root.mainloop()
        
    def login(self):
        self.root.destroy()
        userlogin.login()

    def back(self):
        self.root.destroy()
        first_screen.welcome()

    def register(self):
        self.root.destroy()
        user_register.register()

if __name__=="__main__":
    user()

       

      


        

        
      