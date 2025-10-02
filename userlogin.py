from tkinter import*
from PIL import Image, ImageTk
import userpanel
import database
from tkinter import messagebox
import dashboard_user
class login:
    def __init__(self):
        self.root=Tk()
        self.root.title(" User Login screen")
        self.width=self.root.winfo_screenwidth()-100
        self.height=self.root.winfo_screenheight()-100
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)
        

        self.img_bg=Image.open('pastel orange3.jpg')
        self.img_bg_new=self.img_bg.resize((self.width,self.height))
        self.img_bg_tk=ImageTk.PhotoImage(self.img_bg_new)
        self.img_bg_label=Label(self.root,image=self.img_bg_tk)
        self.img_bg_label.place(x=0,y=0)

        self.img=Image.open('loginimg.jpg')
        self.img_new=self.img.resize((550,550))
        self.img_new_tk=ImageTk.PhotoImage(self.img_new)
        self.img_label=Label(self.root,image=self.img_new_tk)
        self.img_label.place(x=590,y=33)

        self.frame1=Frame(self.root,bg="#494a9e",width=567,height=553)
        self.frame1.place(x=36,y=33)

        # self.frame2=Frame(self.root,bg="#fcfffd",width=495,height=470)
        # self.frame2.place(x=72,y=73)

        self.img1=Image.open('login icon.jpg')
        self.img1_new=self.img1.resize((140,140))
        self.img1_new_tk=ImageTk.PhotoImage(self.img1_new)
        self.img1_label=Label(self.root,image=self.img1_new_tk)
        self.img1_label.place(x=230,y=83)

        self.label=Label(self.root,bg="#494a9e",font=('times new roman',17,'bold'),text="EMAIL",fg="#fcfffd")
        self.label.place(x=90,y=275)
        self.email_box=Entry(self.root,font=('times new roman',15,'bold'),bg="#fcfffd")
        self.email_box.place(x=280,y=280)

        self.label1=Label(self.root,bg="#494a9e",text="PASSWORD",font=('times new roman',17,'bold'),fg="#fcfffd")
        self.label1.place(x=90,y=335)
        self.pass_box=Entry(self.root,font=('times new roman',15,'bold'),bg="#fcfffd")
        self.pass_box.place(x=280,y=340)

        self.button=Button(self.root,text='SIGN IN',font=('times new roman',15,'bold'),bg="#fcfffd",bd=2,relief="solid",command=self.user)
        self.button.place(x=395,y=400)

        self.imgback=Image.open('back.jpg')
        self.imgback_new=self.imgback.resize((30,30))
        self.imgback_tk=ImageTk.PhotoImage(self.imgback_new)
        self.back_button=Button(self.root, text="BACK",image=self.imgback_tk,command=self.back,bg="white",bd=2,relief="solid")
        self.back_button.place(x=0,y=0)


        self.root.mainloop()

    def back(self):
        self.root.destroy()
        userpanel.user() 

    def user(self):
        data=(self.email_box.get(),self.pass_box.get())
        print(data)

        res=database.getallpeople(data)
        if res:
            messagebox.showinfo("Success"," User login Successfully")
            self.root.destroy()
            dashboard_user.userboard(res)
        else:
            messagebox.showerror("Error","User not exist")

if __name__=="__main__":
    login()

