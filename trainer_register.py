from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
from tkinter import ttk
from tkcalendar import DateEntry
import shutil
import os
from datetime import date
import database
import trainerlogin
class tregister:
    def __init__(self):
        self.root=Tk()
        self.root.title("Register Screen For Trainer")
        self.width=self.root.winfo_screenwidth()-100
        self.height=self.root.winfo_screenheight()-100

        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)

        self.img_bg=Image.open('pastel orange3.jpg')
        self.img_bg_new=self.img_bg.resize((self.width,self.height))
        self.img_bg_tk=ImageTk.PhotoImage(self.img_bg_new)
        self.img_bg_label=Label(self.root,image=self.img_bg_tk)
        self.img_bg_label.place(x=0,y=0)
        
        self.frame1=Frame(self.root,background="#fcfffd",width=1110,height=550)
        self.frame1.place(x=36,y=35)

        self.img=Image.open('create account logo.png')
        self.img_new=self.img.resize((125,120))
        self.img_tk=ImageTk.PhotoImage(self.img_new)
        self.img_label=Label(self.root,image=self.img_tk)
        self.img_label.place(x=1010,y=80)

        
        self.labelstart=Label(self.root,text="TRAINER  REGISTRATION  PORTAL",font=('times new roman',15,'bold'),bg="#050505",width=92,fg="#fcfffd")
        self.labelstart.place(x=36,y=45)

        self.label=Label(self.root,text="NAME",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label.place(x=45,y=90)

        self.name_box=Entry(self.root,font=('times new roman',14,'bold'),background="#FFB6C1")
        self.name_box.place(x=500,y=90)

        self.label1=Label(self.root,text="EMAIL",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label1.place(x=45,y=130)

        self.email_box=Entry(self.root,font=('times new roman',14,'bold'),background="#FFB6C1")
        self.email_box.place(x=500,y=130)

        self.label2=Label(self.root,text="PASSWORD",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label2.place(x=45,y=170)

        self.password_box=Entry(self.root,font=('times new roman',14,'bold'),background="#FFB6C1",show="*")
        self.password_box.place(x=500,y=170)

        self.label3=Label(self.root,text="AGE",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label3.place(x=45,y=210)

        self.age_box=Entry(self.root,font=('times new roman',14,'bold'),bg="#FFB6C1")
        self.age_box.place(x=500,y=210)
                           
        self.label4=Label(self.root,text="GENDER",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label4.place(x=45,y=250)

        self.radiobutton_value=StringVar()

        self.radiobutton1=Radiobutton(self.root,text="MALE",width=11,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_value,value='MALE')
        self.radiobutton1.place(x=500,y=250)

        self.radiobutton2=Radiobutton(self.root,text="FEMALE",width=11,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_value,value='FEMALE')
        self.radiobutton2.place(x=640,y=250)

        self.radiobutton3=Radiobutton(self.root,text="OTHERS",width=11,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_value,value="OTHERS")
        self.radiobutton3.place(x=780,y=250)

        self.label9=Label(self.root,text="DOB",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label9.place(x=45,y=290)

        self.dob=DateEntry(self.root,date_pattern='yyyy/mm/dd',maxdate=date.today(),width=30)
        self.dob.place(x=500,y=290)

        self.label5=Label(self.root,text="ADDRESS",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label5.place(x=45,y=330)

        self.adress_box=Entry(self.root,font=('times new roman',14,'bold'),background="#FFB6C1")
        self.adress_box.place(x=500,y=330)

        self.label6=Label(self.root,text="MOBILE NUMBER",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label6.place(x=45,y=370)

        self.mobile_box=Entry(self.root,font=('times new roman',14,'bold'),background="#FFB6C1")
        self.mobile_box.place(x=500,y=370)

        self.label7=Label(self.root,text="YEARS OF EXPERIENCE",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label7.place(x=45,y=410)

        self.radiobutton_yoe=StringVar()
        expradiobutton1=Radiobutton(self.root,text="1-5 YRS",width=11,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_yoe,value="1-5 YRS")
        expradiobutton1.place(x=500,y=410)
        expradiobutton2=Radiobutton(self.root,text="5-10 YRS",width=11,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_yoe,value="5-10 YRS")
        expradiobutton2.place(x=640,y=410)
        expradiobutton3=Radiobutton(self.root,text="10 AND MORE",width=11,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_yoe,value="10 AND MORE")
        expradiobutton3.place(x=780,y=410)

        self.label8=Label(self.root,text="PREFERRED COMMUNICATION LANGUAGE ",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label8.place(x=45,y=450)
        self.radiobutton_com=StringVar()
        
        langradiobutton1=Radiobutton(self.root,text="ENGLISH",width=11,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_com,value="ENGLISH")
        langradiobutton1.place(x=500,y=450)
        langradiobutton2=Radiobutton(self.root,text="HINDI",width=11,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_com,value="HINDI")
        langradiobutton2.place(x=640,y=450)
        langradiobutton3=Radiobutton(self.root,text="PUNJABI",width=11,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_com,value="PUNJABI")
        langradiobutton3.place(x=780,y=450)

        # self.label8=Label(self.root,text="AVAILABLE TIME SLOTS ",bg="#fcfffd",font=('times new roman',14,'bold'))
        # self.label8.place(x=45,y=490)
        # self.radiobutton_time=StringVar
        
        # timeradiobutton1=Radiobutton(self.root,text="8AM-10AM",width=11,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_time,value="8AM-10AM")
        # timeradiobutton1.place(x=500,y=490)
        # timeradiobutton2=Radiobutton(self.root,text="10AM-12PM",width=11,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_time,value="10MA-12AM")
        # timeradiobutton2.place(x=640,y=490)
        # timeradiobutton3=Radiobutton(self.root,text="4PM-6PM",width=11,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_time,value="4PM-6PM")
        # timeradiobutton3.place(x=780,y=490)

        self.label9=Label(self.root,text="UPLOAD YOUR PHOTO",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label9.place(x=45,y=490)

        self.but1=Button(self.root,text="UPLOAD",font=('times new roman',14,'bold'),bd=2,relief='solid',bg="#FFB6C1",command=self.upload_file)
        self.but1.place(x=500,y=490)

        
        self.button1=Button(self.root,text="SUBMIT",font=('times new roman',15,'bold'),bg="#FFB6C1", bd=2, relief="solid",command=self.getval)
        self.button1.place(x=1029,y=545)

        self.root.mainloop()  

    def upload_file(self):
       # Open a file dialog and select a file
        self.file_path = filedialog.askopenfilename()
    
        if self.file_path:
            try:
            # Define the target directory to save the file
                self.target_directory = "uploaded_files"
            
            # Create the target directory if it doesn't exist
                if not os.path.exists(self.target_directory):
                    os.makedirs(self.target_directory)
            
            # Extract the file name from the file path
                self.file_name = os.path.basename(self.file_path)
            
            # Define the target file path
                self.target_file_path = os.path.join(self.target_directory, self.file_name)
            
                print("Target directory ",self.target_directory)
                print("Target file path ",self.target_file_path)   # save this path in database
                # Copy the selected file to the target directory
                shutil.copy(self.file_path, self.target_file_path)
                # Show a success message
                messagebox.showinfo("Success", f"File '{self.file_name}' uploaded successfully!")
                # self.display_uploaded_image(self.target_file_path)

                self.imgii = Image.open(self.file_path)
                self.imgii_new = self.imgii.resize((125,120))
                self.imgii_tk = ImageTk.PhotoImage(self.imgii_new)
            
                
                self.img_label.config(image=self.imgii_tk)
                self.img_label.image= self.imgii_tk
        
            except Exception as e:
            # Show an error message if something goes wrong
                messagebox.showerror("Error", f"Failed to upload file: {str(e)}")
        else:
            messagebox.showwarning("No File", "No file was selected.")

    def getval(self):
        data=(self.name_box.get(),self.email_box.get(),self.password_box.get(),self.age_box.get(),self.radiobutton_value.get(),self.dob.get(),self.adress_box.get(),self.mobile_box.get(),self.radiobutton_yoe.get(),self.radiobutton_com.get(),self.target_file_path)
    
        res=database.registertrainer(data)
        if res:
            messagebox.showinfo("Database","Trainer Registered Successfully")
            trainerlogin.login()
        else:
            messagebox.showerror("Error","Not Registered")
    
            
if __name__=="__main__":
    tregister()
