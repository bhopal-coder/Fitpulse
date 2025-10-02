from tkinter import *
from PIL import Image,ImageTk
import bmi_category1
import database
from tkinter import messagebox
class BMI_calc:
    def __init__(self,res):
        self.root=Tk()
        self.root.title("BMI Calculator")
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

        # self.frame1=Frame(self.root,bg="white",width=self.width,height=self.height)
        # self.frame1.place(x=0,y=0)

        self.image1=Image.open('bestbmi1.jpg')
        self.image1_new=self.image1.resize((580,584))
        self.image1_new_tk=ImageTk.PhotoImage(self.image1_new)
        self.image1_label=Label(self.root,image=self.image1_new_tk,bg="white")
        self.image1_label.place(x=20,y=20)

        self.frame1=Frame(self.root,bg="#b1e5fa",width=550,height=588)
        self.frame1.place(x=600,y=20)

       

        self.label1=Label(self.root,text="BMI  CALCULATOR",font=('times new roman',17,'bold'),bg="#b1e5fa",fg="#0a0a0a")
        self.label1.place(x=750,y=50)

        self.frm=Frame(self.root,bg="#fcfffd",width=366,height=160)
        self.frm.place(x=690,y=100)

        self.image2=Image.open('squ.jpg')
        self.image2_new=self.image2.resize((150,150))
        self.image2_new_tk=ImageTk.PhotoImage(self.image2_new)
        self.image2_label=Label(self.root,image=self.image2_new_tk,bg="#fcfffd")
        self.image2_label.place(x=700,y=100)

        self.img=Image.open('squ.jpg')
        self.img_new=self.img.resize((150,150))
        self.img_new_tk=ImageTk.PhotoImage(self.img_new)
        self.img_label=Label(self.root,image=self.img_new_tk,bg="#fcfffd")
        self.img_label.place(x=890,y=100)

        

        self.label=Label(self.root,text="HEIGHT",font=('times new roman',15,'bold'),bg="#fcfffd",fg="#0a0a0a")
        self.label.place(x=735,y=120)

        self.label2=Label(self.root,text="WEIGHT",font=('times new roman',15,'bold'),bg="#fcfffd",fg="#0a0a0a")
        self.label2.place(x=920,y=120)

        self.height=float(res[8])
        htlabel=Label(self.root,text=f"{self.height}",font=('times new roman',17,'bold'),bg="#fcfffd",fg="#0a0a0a")
        htlabel.place(x=750,y=205)

        self.weight= float(res[7])
        wtlabel=Label(self.root,text=f"{self.weight}",font=('times new roman',17,'bold'),bg="#fcfffd",fg="#0a0a0a")
        wtlabel.place(x=945,y=205)

        self.btn=Button(self.root,text="VIEW BMI",font=('times new roman',15,'bold'),bg="#fcfffd",fg="#0a0a0a",relief='solid',command=self.BMI)
        self.btn.place(x=1000,y=300)   

        self.btn1=Button(self.root,text="VIEW BODY CATEGORY",font=('times new roman',15,'bold'),fg="#0a0a0a",relief='solid',bg="#fcfffd",command=self.nextscreen)
        self.btn1.place(x=870,y=450)

       

        
        # self.frame2=Frame(self.root,bg='#fcfffd',width=530,height=300)
        # self.frame2.place(x=20,y=300)


       
        # self.image2=Image.open('scale.jpg')
        # self.image2_new=self.image2.resize((53,274))
        # self.image2_new_tk=ImageTk.PhotoImage(self.image2_new)
        # self.image2_label=Label(self.root,image=self.image2_new_tk,bg="#fcfffd")
        # self.image2_label.place(x=40,y=320)

        # self.image3=Image.open('man.jpg')
        # self.image3_new=self.image3.resize((53,260))
        # self.image3_new_tk=ImageTk.PhotoImage(self.image3_new)
        # self.image3_label=Label(self.root,image=self.image3_new_tk,bg="#fcfffd")
        # self.image3_label.place(x=100,y=320)

        self.root.mainloop()

    def BMI(self):
        self.height_metre=self.height/100
        bmi=(self.weight)/(self.height_metre*self.height_metre)
        print(bmi)

        data=bmi
        id=self.res[0]
        b=database.savebmi(id,data)

        self.labelbmi=Label(self.root,text=bmi,font=('times new roman',17,'bold'),bg="#b1e5fa",fg="#0a0a0a")
        self.labelbmi.place(x=800,y=370)
      
    def nextscreen(self):
        self.height_metre=self.height/100
        bmi=(self.weight)/(self.height_metre*self.height_metre)
        self.root.destroy()
        bmi_category1.BMI_cate(bmi,self.res)


     
        

    
if __name__=="__main__":
    res="1111111111"
    BMI_calc(res)