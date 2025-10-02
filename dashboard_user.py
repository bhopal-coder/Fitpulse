from tkinter import *
from PIL import Image,ImageTk
import dash_user_details
import bmi_calculator1
import bmi_category1
import userlogin
import user_diet 
class userboard:
    def __init__(self,res):
        self.root=Tk()
        self.root.title("Dashboard for user")
        self.res=res
         
        self.width=self.root.winfo_screenwidth()-100
        self.height=self.root.winfo_screenheight()-100
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)
        
        self.image=Image.open('pastel orange3.jpg')
        self.image_new=self.image.resize((self.width,self.height))
        self.image_new_tk=ImageTk.PhotoImage(self.image_new)
        self.image_label=Label(self.root,image=self.image_new_tk)
        self.image_label.place(x=0,y=0)
          
        self.frame1=Frame(self.root,bg="#0a0a0a",width=1140,height=100)
        self.frame1.place(x=20,y=20)

        self.image1=Image.open('userimage.jpg')
        self.image1_new=self.image1.resize((526,480))
        self.image1_new_tk=ImageTk.PhotoImage(self.image1_new)
        self.image1_label=Label(self.root,image=self.image1_new_tk)
        self.image1_label.place(x=630,y=120)

        self.frame1=Frame(self.root,bg="#fcfffd",width=630,height=483)
        self.frame1.place(x=20,y=121)

        self.image2=Image.open('logoproj-Photoroom.png')
        self.image2_new=self.image2.resize((100,100))
        self.image2_new_tk=ImageTk.PhotoImage(self.image2_new)
        self.image2_label=Label(self.root,image=self.image2_new_tk)
        self.image2_label.place(x=20,y=20) 




          

        
        self.button1=Button(self.root,text="Personal Info",font=('Times new roman',15,'bold'),bg="#0a0a0a",bd=0,relief="solid",fg="#fcfffd",command=self.user)
        self.button1.place(x=150,y=70)

        self.button2=Button(self.root,text="Body BMI and Category",font=('Times new roman',15,'bold'),bg="#0a0a0a",bd=0,relief="solid",fg="#fcfffd",command=self.bmi)
        self.button2.place(x=290,y=70)

        self.button6=Button(self.root,text="Suggested Diet",font=('Times new roman',15,'bold'),bg="#0a0a0a",bd=0,relief="solid",fg="#fcfffd",command=self.diet)
        self.button6.place(x=530,y=70)

        self.button8=Button(self.root,text="LogOut",font=('Times new roman',15,'bold'),bg="#0a0a0a",bd=1,relief="solid",fg="#fcfffd",command=self.logout)
        self.button8.place(x=1020,y=70)


        self.label=Label(self.root,text="Fitness is not about being better than",bg="#fcfffd",fg="#0a0a0a",font=('times new roman',17,'bold'))
        self.label.place(x=70,y=280)

        self.label1=Label(self.root,text="someone else . It's about being better",bg="#fcfffd",fg="#0a0a0a",font=('times new roman',17,'bold'))
        self.label1.place(x=70,y=320)

        self.label2=Label(self.root,text="than you used to be .",bg="#fcfffd",fg="#0a0a0a",font=('times new roman',17,'bold'))
        self.label2.place(x=70,y=360)

        
        


        print(res)
        self.root.mainloop()


    def user(self):
        self.root.destroy()
        dash_user_details.udetails(self.res)

    def bmi(self):
        self.root.destroy()
        bmi_calculator1.BMI_calc(self.res)

    def logout(self):
        self.root.destroy()
        userlogin.login()

    def diet(self):
        self.root.destroy()
        user_diet.diet(self.res)



if __name__=="__main__":
    res="anystring"
    userboard(res)

            