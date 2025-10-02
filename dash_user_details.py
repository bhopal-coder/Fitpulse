from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import update_user_register
import dashboard_user
class udetails:
    def __init__(self,res):
        self.root=Tk()
        self.root.title("User Details")
        self.res=res
        print(self.res)
        self.width=self.root.winfo_screenwidth()-100
        self.height=self.root.winfo_screenheight()-100
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)
        
        self.image=Image.open('pastel orange3.jpg')
        self.image_new=self.image.resize((self.width,self.height))
        self.image_new_tk=ImageTk.PhotoImage(self.image_new)
        self.image_label=Label(self.root,image=self.image_new_tk)
        self.image_label.place(x=0,y=0)

        self.image1=Image.open('info.jpg')
        self.image1_new=self.image1.resize((400,582))
        self.image1_new_tk=ImageTk.PhotoImage(self.image1_new)
        self.image1_label=Label(self.root,image=self.image1_new_tk)
        self.image1_label.place(x=20,y=20)

        self.frame1=Frame(self.root,bg="#133a78",width=740,height=584)
        self.frame1.place(x=420,y=20)

        self.x=res[10]

        self.imgi=Image.open(self.x)
        self.imgi_new=self.imgi.resize((100,100))
        self.imgi_tk=ImageTk.PhotoImage(self.imgi_new)
        self.imgi_label=Label(self.root,image=self.imgi_tk)
        self.imgi_label.place(x=720,y=30)


        self.label1=Label(self.root,text="NAME",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.label1.place(x=550,y=140)

        self.name=res[1]
        self.namelabel=Label(self.root,text=f"{self.name}",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.namelabel.place(x=920,y=140)




        self.label=Label(self.root,text="AGE",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.label.place(x=550,y=180)

        self.age=res[2]
        self.agelabel=Label(self.root,text=f"{self.age}",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.agelabel.place(x=920,y=180)

        self.label1=Label(self.root,text="EMAIL",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.label1.place(x=550,y=220)

        self.email=res[3]
        self.emaillabel=Label(self.root,text=f"{self.email}",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.emaillabel.place(x=920,y=220)

        self.label2=Label(self.root,text="PASSWORD",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.label2.place(x=550,y=260)

        self.pas=res[4]
        self.paslabel=Label(self.root,text=f"{self.pas}",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.paslabel.place(x=920,y=260)

        self.label3=Label(self.root,text="GENDER",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.label3.place(x=550,y=300)

        self.gender=res[5]
        self.genderlabel=Label(self.root,text=f"{self.gender}",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.genderlabel.place(x=920,y=300)

        self.label4=Label(self.root,text="DOB",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.label4.place(x=550,y=340)

        self.dob=res[6]
        self.doblabel=Label(self.root,text=f"{self.dob}",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.doblabel.place(x=920,y=340)

        self.label5=Label(self.root,text="WEIGHT",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.label5.place(x=550,y=380)

        self.weight=res[7]
        self.weightlabel=Label(self.root,text=f"{self.weight}",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.weightlabel.place(x=920,y=380)

        self.label6=Label(self.root,text="HEIGHT",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.label6.place(x=550,y=420)

        self.height=res[8]
        self.heightlabel=Label(self.root,text=f"{self.height}",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.heightlabel.place(x=920,y=420)

        self.label7=Label(self.root,text="PHONE NUMBER",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.label7.place(x=550,y=460)

        self.ph=res[9]
        self.phlabel=Label(self.root,text=f"{self.ph}",font=('times new roman',14,'bold'),bg="#133a78",fg="#fcfffd")
        self.phlabel.place(x=920,y=460)

        self.btn=Button(self.root,text="EDIT",font=('times new roman',14,'bold'),bg="#fcfffd",fg="#133a78",bd=2,relief='solid',command=self.edit)
        self.btn.place(x=1050,y=500)

        self.imgback=Image.open('back.jpg')
        self.imgback_new=self.imgback.resize((30,30))
        self.imgback_tk=ImageTk.PhotoImage(self.imgback_new)
        self.back_button=Button(self.root, text="BACK",image=self.imgback_tk,command=self.back,bg="white",bd=2,relief="solid")
        self.back_button.place(x=0,y=0)





        self.root.mainloop()

    def edit(self):
        ru=messagebox.showwarning("Edit","Do You rearlly want to Edit ")
        if ru:
            self.root.destroy()
            update_user_register.uregister(self.res)

    def back(self):
        self.root.destroy()
        dashboard_user.userboard(self.res)



if __name__=="__main__":
    res="abcdefghijklmnop"
    udetails(res)




