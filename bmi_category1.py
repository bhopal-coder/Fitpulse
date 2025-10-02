from tkinter import *
from PIL import Image,ImageTk
import database
from tkinter import messagebox
import user_diet
import dashboard_user
import streamlit as st
class BMI_cate:
    def __init__(self,bmi,res):
        self.root=Tk()
        self.root.title("BMI Category")
        self.bmi=bmi
        self.res=res
        
        

        self.width=self.root.winfo_screenwidth()-100
        self.height=self.root.winfo_screenheight()-100
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)

        self.image1=Image.open('fitimage.png')
        self.image1_new=self.image1.resize((self.width,self.height))
        self.image1_tk=ImageTk.PhotoImage(image=self.image1_new)
        self.image1.label=Label(self.root,image=self.image1_tk)
        self.image1.label.place(x=0,y=0)

        self.frame=Frame(self.root,bg="#F2D2BD",width=630,height=570)
        self.frame.place(x=20,y=20)
        self.label=Label(self.root,text='BMI CATEGORY',font=('times new roman',15,'bold'),bg="#fcfffd",fg="#0a0a0a",width=20)
        self.label.place(x=20,y=30)

        self.food='''CARBOHYDRATES : Sweet potatoes, Brown rice, Whole-Grain Bread, Corn, Oats, Bananas, Avacado
                          FATS : Olive Oil, Coconut Oil, Milk, Cheese, Yoghurt, Pistachios, Nuts, Ghee , Full-fat yogurt
                          PROTEINS : Legumes, Soy products, Chicken, Eggs, Beans, Lentils, Chickpeas, Spinach, Borocoli
                          VITAMINS AND MINERALS: Some sources of vitamins like Carrots, Kale, Butternut squash, Oranges, Kiwi, Bellpeper
                          ROUGHAGE: Oats, Brown rice, Barley, Apples, pears, Leafy greens, Turnips, Almonds, Flex seeds '''




        if bmi<18.5:
            self.label1=Label(self.root,text='UNDERWEIGHT',font=('times new roman',15,'bold'),bg="#F2D2BD",fg="#0a0a0a")
            self.label1.place(x=60,y=140)
             
            self.imageu=Image.open('underweight.jpg')
            self.imageu_new=self.imageu.resize((300,150))
            self.imageu_tk=ImageTk.PhotoImage(image=self.imageu_new)
            self.imageu.label=Label(self.root,image=self.imageu_tk,bg="#F2D2BD")
            self.imageu.label.place(x=310,y=110)
           
            self.quote1=Label(self.root,text="You have lower weight,",font=('times mew roman',13,'bold'),bg="#F2D2BD")
            self.quote1.place(x=50,y=250)
            self.quote2=Label(self.root,text="than normal body!",font=('times mew roman',13,'bold'),bg="#F2D2BD")
            self.quote2.place(x=50,y=275)

            self.labelu=Label(self.root,text="  POTENTIAL  ISSUES  DUE  TO  UNDERWEIGHT CONDITION:",font=('times new roman',14,'bold'),bg="#fcfffd",fg="#0a0a0a")
            self.labelu.place(x=20,y=320)

            self.labelua=Label(self.root,text=" Higher risk for bone loss and fractures. ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelua.place(x=50,y=370)

            self.labelub=Label(self.root,text=" Results in chronic fatigue and low energy levels.  ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelub.place(x=50,y=405)

            self.labeluc=Label(self.root,text=" Can lead to a slow heart rate (bradycardia), low blood pressure  ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labeluc.place(x=50,y=445)

            self.labelud=Label(self.root,text=" (hypotension), and other heart-related issues.",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelud.place(x=50,y=470)

            self.labelue=Label(self.root,text=" Can contribute to mental health issues like depression and anxiety . ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelue.place(x=50,y=510)

            
            

            
           
                    
        
       
        elif bmi>=18.5 and bmi<=24.9:
            self.label2=Label(self.root,text='NORMAL WEIGHT',font=('times new roamn',15,'bold'),bg="#F2D2BD")
            self.label2.place(x=60,y=140)

            self.imagen=Image.open('normal.jpg')
            self.imagen_new=self.imagen.resize((300,150))
            self.imagen_tk=ImageTk.PhotoImage(image=self.imagen_new)
            self.imagen.label=Label(self.root,image=self.imagen_tk,bg="#F2D2BD")
            self.imagen.label.place(x=310,y=110)
           
            self.quoten1=Label(self.root,text="You have normal weight",font=('times mew roman',13,'bold'),bg="#F2D2BD")
            self.quoten1.place(x=50,y=250)
            self.quoten2=Label(self.root,text="It indicates that you are healthy",font=('times mew roman',13,'bold'),bg="#F2D2BD")
            self.quoten2.place(x=50,y=275)

            self.labeln=Label(self.root,text=" SUGGESTIONS:",font=('times new roman',14,'bold'),bg="#fcfffd",fg="#0a0a0a")
            self.labeln.place(x=20,y=320)

            self.labelna=Label(self.root,text=" Keep focusing on a nutritious and balanced diet. ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelna.place(x=50,y=370)

            self.labelub=Label(self.root,text=" Regularly assess and manage stress through techniques ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelub.place(x=50,y=410)

            self.labeluc=Label(self.root,text=" like deep breathing and yoga ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labeluc.place(x=50,y=435)

            self.labelud=Label(self.root,text=" Maintain proper hydration by drinking water throughout the day. ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelud.place(x=50,y=475)

           

        elif bmi>=25 and bmi<=29.9:

            self.label3=Label(self.root,text='OVERWEIGHT',font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.label3.place(x=60,y=140)

            self.imageo=Image.open('overweight.jpg')
            self.imageo_new=self.imageo.resize((300,150))
            self.imageo_tk=ImageTk.PhotoImage(image=self.imageo_new)
            self.imageo.label=Label(self.root,image=self.imageo_tk,bg="#F2D2BD")
            self.imageo.label.place(x=310,y=110)
           
            self.quoteo1=Label(self.root,text="It indicates that you are slightly overweight,",font=('times mew roman',13,'bold'),bg="#F2D2BD")
            self.quoteo1.place(x=50,y=250)
            self.quoteo2=Label(self.root,text="a health care professional may advise to lose some!",font=('times mew roman',13,'bold'),bg="#F2D2BD")
            self.quoteo2.place(x=50,y=275)

            self.labelo=Label(self.root,text=" POTENTIAL ISSUES DUE TO OVERWEIGHT CONDITION:",font=('times new roman',14,'bold'),bg="#fcfffd",fg="#0a0a0a")
            self.labelo.place(x=20,y=320)

            self.labeloa=Label(self.root,text=" Higher risk for coronary artery disease and stroke.",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labeloa.place(x=50,y=370)

            self.labelob=Label(self.root,text=" Risk of Osteoarthritis in future. ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelob.place(x=50,y=410)

            self.labeloc=Label(self.root,text=" Increases the risk of gallstones and gallbladder disease. ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labeloc.place(x=50,y=435)

            self.labelod=Label(self.root,text="  In females, it can contribute to hormonal imbalances causing PCOS. ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelod.place(x=50,y=475)

           

            
        elif bmi>=30 and bmi<=34.9:
            self.labelob=Label(self.root,text='OBESITY',font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelob.place(x=60,y=140)

            self.imageob=Image.open('obese.jpg')
            self.imageob_new=self.imageob.resize((300,150))
            self.imageob_tk=ImageTk.PhotoImage(image=self.imageob_new)
            self.imageob.label=Label(self.root,image=self.imageob_tk,bg="#F2D2BD")
            self.imageob.label.place(x=310,y=110)
           
            self.quoteob1=Label(self.root,text="Heath may be at risk if they ",font=('times mew roman',13,'bold'),bg="#F2D2BD")
            self.quoteob1.place(x=50,y=250)
            self.quoteob2=Label(self.root,text="you do not loose weight",font=('times mew roman',13,'bold'),bg="#F2D2BD")
            self.quoteob2.place(x=50,y=275)

            self.labelob3=Label(self.root,text=" POTENTIAL ISSUES DUE TO OBESITY ",font=('times new roman',14,'bold'),bg="#fcfffd",fg="#0a0a0a")
            self.labelob3.place(x=20,y=320)

            self.labelob3a=Label(self.root,text=" Major risk factor for developing insulin resistance and type 2 diabetes.",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelob3a.place(x=50,y=370)

            self.labelob4=Label(self.root,text=" Excess weight can worsen asthma symptoms and reduce lung function. ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelob4.place(x=50,y=410)

            self.labelob5=Label(self.root,text=" Increased risk of cancer of the lining of the uterus.",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelob5.place(x=50,y=435)

            self.labelob6=Label(self.root,text=" Increased risk of kidney damage in future. ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.labelob6.place(x=50,y=475)

           
           

        elif bmi>35:
            self.label5=Label(self.root,text='EXTREMELY OBESE',font=('times new roman',15,'bold'),bg="#F2D2BD",fg="#0a0a0a")
            self.label5.place(x=60,y=140)

            self.image2=Image.open('extremely obese 1.jpg')
            self.image2_new=self.image2.resize((300,150))
            self.image2_tk=ImageTk.PhotoImage(image=self.image2_new)
            self.image2.label=Label(self.root,image=self.image2_tk,bg="#F2D2BD")
            self.image2.label.place(x=310,y=110)
           
            self.quote9=Label(self.root,text="Health is at major risk,",font=('times mew roman',13,'bold'),bg="#F2D2BD")
            self.quote9.place(x=50,y=250)
            self.quote10=Label(self.root,text="Please consult a health care professional  as early as possible!",font=('times mew roman',13,'bold'),bg="#F2D2BD")
            self.quote10.place(x=50,y=275)

            self.label6=Label(self.root,text="  POTENTIAL  ISSUES  DUE  TO  EXTREME  OBESITY:",font=('times new roman',14,'bold'),bg="#fcfffd",fg="#0a0a0a")
            self.label6.place(x=20,y=320)

            self.label6a=Label(self.root,text=" Increased risk of heart disease, high blood pressure, stroke, and heart  ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.label6a.place(x=50,y=370)

            self.label6b=Label(self.root,text=" failure due to the added strain on the cardiovascular system. ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.label6b.place(x=50,y=395)

            self.label6c=Label(self.root,text=" Higher likelihood of developing insulin resistance and type 2 diabetes,",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.label6c.place(x=50,y=430)

            self.label6d=Label(self.root,text=" which can lead to neuropathy and retinopathy.",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.label6d.place(x=50,y=455)

            self.label6e=Label(self.root,text=" Higher risk of gastrointestinal issues such as gastroesophageal reflux ",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.label6e.place(x=50,y=490)

            self.label6f=Label(self.root,text=" disease (GERD), fatty liver disease, and gallbladder problems .",font=('times new roman',14,'bold'),bg="#F2D2BD")
            self.label6f.place(x=50,y=515)
        
        self.imgback=Image.open('back.jpg')
        self.imgback_new=self.imgback.resize((30,30))
        self.imgback_tk=ImageTk.PhotoImage(self.imgback_new)
        self.back_button=Button(self.root, text="BACK",image=self.imgback_tk,bg="white",bd=2,relief="solid",command=self.back)
        self.back_button.place(x=0,y=0)

        self.root.mainloop()       
        # st.session_state("client_id")=res[0]
    def back(self):
        self.root.destroy()
        dashboard_user.userboard(self.res)

if __name__=="__main__":
    bmi="00000000000120000"
    BMI_cate(bmi)