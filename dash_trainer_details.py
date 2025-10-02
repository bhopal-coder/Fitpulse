from tkinter import *
from PIL import Image,ImageTk
import dashboard_trainer
from tkinter import messagebox
import update_trainer_register
class details:
    def __init__(self,res):
        self.root=Tk()
        self.root.title("Trainer Details")
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

        self.frame=Frame(self.root,bg="#080a36",width=380,height=582)
        self.frame.place(x=20,y=20)

        self.frame1=Frame(self.root,bg="#080a36",width=740,height=582)
        self.frame1.place(x=420,y=20)

        self.frame3=Frame(self.root,bg="#fcfffd",width=740,height=15)
        self.frame3.place(x=420,y=25)

        self.frame5=Frame(self.root,bg="#fcfffd",width=740,height=15)
        self.frame5.place(x=420,y=580)

        self.frame4=Frame(self.root,bg="#fcfffd",width=380,height=15)
        self.frame4.place(x=20,y=25)

        self.frame6=Frame(self.root,bg="#fcfffd",width=380,height=15)
        self.frame6.place(x=20,y=580)

        self.label=Label(self.root,text="FITPULSE",bg="#080a36",fg="#fcfffd",font=('times new roman',25,'bold'))
        self.label.place(x=130,y=45)

        self.x=res[11]
        print(self.x)
        
        self.imgi=Image.open(self.x)
        self.imgi_new=self.imgi.resize((120,120))
        self.imgi_tk=ImageTk.PhotoImage(self.imgi_new)
        self.imgi_label=Label(self.root,image=self.imgi_tk)
        self.imgi_label.place(x=150,y=150)

        self.name=res[1]
        self.namelabel=Label(self.root,text=f"{self.name}",font=('times new roman',20,'bold'),bg="#080a36",width=15,fg="#fcfffd")
        self.namelabel.place(x=60,y=400)

        self.label2=Label(self.root,text="EMAIL",bg="#080a36",font=('times new roman',14,'bold'),fg="#fcfffd")
        self.label2.place(x=450,y=60)

        self.email=res[2]
        self.emaillabel=Label(self.root,text=f"{self.email}",font=('times new roman',14,'bold'),bg="#080a36",fg="#fcfffd")
        self.emaillabel.place(x=920,y=60)

        self.label3=Label(self.root,text="PASSWORD",bg="#080a36",font=('times new roman',14,'bold'),fg="#fcfffd")
        self.label3.place(x=450,y=100)

        self.pas=res[3]
        self.paslabel=Label(self.root,text=f"{self.pas}",font=('times new roamn',14,'bold'),bg="#080a36",fg="#fcfffd")
        self.paslabel.place(x=920,y=100)

        self.label4=Label(self.root,text="AGE",bg="#080a36",font=('times new roman',14,'bold'),fg="#fcfffd")
        self.label4.place(x=450,y=140)
        
        self.age=res[4]
        self.agelabel=Label(self.root,text=f"{self.age}",font=('times new roman',14,'bold'),bg="#080a36",fg="#fcfffd")
        self.agelabel.place(x=920,y=140)

        self.label5=Label(self.root,text="GENDER",bg="#080a36",font=('times new roman',14,'bold'),fg="#fcfffd")
        self.label5.place(x=450,y=180)

        self.gender=res[5]
        self.genderlabel=Label(self.root,text=f"{self.gender}",font=('times new roman',14,'bold'),bg="#080a36",fg="#fcfffd")
        self.genderlabel.place(x=920,y=180)

        self.label6=Label(self.root,text="DATE OF BIRTH",bg="#080a36",font=('times new roman',14,'bold'),fg="#fcfffd")
        self.label6.place(x=450,y=220)

        self.dob=res[6]
        self.doblabel=Label(self.root,text=f"{self.dob}",font=('times new roman',14,'bold'),bg="#080a36",fg="#fcfffd")
        self.doblabel.place(x=920,y=220)

        self.label7=Label(self.root,text="ADDRESS",bg="#080a36",font=('times new roman',14,'bold'),fg="#fcfffd")
        self.label7.place(x=450,y=260) 

        self.add=res[7]
        self.labeladd=Label(self.root,text=f"{self.add}",font=('times new roman',14,'bold'),bg="#080a36",fg="#fcfffd")
        self.labeladd.place(x=920,y=260)

        self.label8=Label(self.root,text="MOBLIE NUMBER",bg="#080a36",font=('times new roman',14,'bold'),fg="#fcfffd")
        self.label8.place(x=450,y=300) 

        self.mn=res[8]
        self.labelmn=Label(self.root,text=f"{self.mn}",font=('times new roman',14,'bold'),bg="#080a36",fg="#fcfffd")
        self.labelmn.place(x=920,y=300)

        self.label9=Label(self.root,text="YEARS OF EXPERIENCE",bg="#080a36",font=('times new roman',14,'bold'),fg="#fcfffd")
        self.label9.place(x=450,y=340) 

        self.yoe=res[9]
        self.labelyoe=Label(self.root,text=f"{self.yoe}",font=('times new roman',14,'bold'),bg="#080a36",fg="#fcfffd")
        self.labelyoe.place(x=920,y=340)

        self.label10=Label(self.root,text="PREFERRED COMMUNICATION LANGUAGE",bg="#080a36",font=('times new roman',14,'bold'),fg="#fcfffd")
        self.label10.place(x=450,y=380) 

        self.pcl=res[10]
        self.labelpcl=Label(self.root,text=f"{self.pcl}",font=('times new roman',14,'bold'),bg="#080a36",fg="#fcfffd")
        self.labelpcl.place(x=920,y=380)

        self.button=Button(self.root,text="EDIT",font=('Times new roman',14,'normal'),bg="#fcfffd",bd=2,relief="solid",width=10,fg="#080a36",command=self.edit)
        self.button.place(x=1000,y=500)
        self.imgback=Image.open('back.jpg')
        self.imgback_new=self.imgback.resize((30,30))
        self.imgback_tk=ImageTk.PhotoImage(self.imgback_new)

        self.back_button=Button(self.root, text="BACK",image=self.imgback_tk,bg="white",bd=2,relief="solid",command=self.back)
        self.back_button.place(x=10,y=10)
        self.root.mainloop()
    def edit(self):
        ru=messagebox.showwarning("Edit","Do You rearlly want to Edit ")
        if ru:
            self.root.destroy()
            update_trainer_register.tregister(self.res)
    def back(self):
        self.root.destroy()
        dashboard_trainer.trainerboard(self.res)

if __name__=="__main__":
    res="muskandeepkaur"
    details(res)

    

    
