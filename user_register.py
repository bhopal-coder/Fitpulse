from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import filedialog, messagebox
from tkcalendar import DateEntry
import shutil
import os
from tkinter import StringVar
from datetime import date
import database
import userpanel
import dashboard_user
import userlogin

class register():
    def __init__(self):
        self.root=Tk()
        self.root.title("User Register")
        self.width=self.root.winfo_screenwidth()-100
        self.height=self.root.winfo_screenheight()-100

        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)

        self.img=Image.open('pastel orange3.jpg')
        self.img_new=self.img.resize((self.width,self.height))
        self.img_tk=ImageTk.PhotoImage(self.img_new)
        self.img_label=Label(self.root,image=self.img_tk)
        self.img_label.place(x=0,y=0)

        # print(self.width)  1180
        # print(self.height)  620

        self.frame=Frame(self.root,bg="#fcfffd",width=1110,height=550)
        self.frame.place(x=36,y=35)

        self.img1=Image.open('create account logo.png')
        self.img1_new=self.img1.resize((125,120))
        self.img1_tk=ImageTk.PhotoImage(self.img1_new)
        self.img1_label=Label(self.root,image=self.img1_tk)
        self.img1_label.place(x=1010,y=80)

        self.label=Label(self.root,text="USER  REGISTRATION  PORTAL",bg="#050505",font=('times new roman',15,'bold'),fg='#fcfffd',width=92)
        self.label.place(x=36,y=45)

        self.label1=Label(self.root,text="NAME",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label1.place(x=45,y=90)

        self.name_entry=Entry(self.root,font=('times new roman',14,'bold'),bg="#FFB6C1")
        self.name_entry.place(x=310,y=90)

        self.label2=Label(self.root,text="AGE",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label2.place(x=45,y=130)

        self.age_box=Entry(self.root,font=('times new roman',14,'bold'),bg="#FFB6C1")
        self.age_box.place(x=310,y=130)

        self.label3=Label(self.root,text="EMAIL",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label3.place(x=45,y=170)

        self.email_box=Entry(self.root,font=('times new roman',14,'bold'),bg="#FFB6C1")
        self.email_box.place(x=310,y=170)

        self.label4=Label(self.root,text="PASSWORD",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label4.place(x=45,y=210)

        
        self.pas_box=Entry(self.root,font=('times new roman',14,'bold'),bg="#FFB6C1")
        self.pas_box.place(x=310,y=210)

        self.label5=Label(self.root,text="GENDER",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label5.place(x=45,y=250)
        
        self.radiobutton_value=StringVar()
        self.radiobutton1=Radiobutton(self.root,text="MALE",width=8,height=1,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_value,value="MALE")
        self.radiobutton1.place(x=310,y=250)

        self.radiobutton2=Radiobutton(self.root,text="FEMALE",width=8,height=1,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_value,value="FEMALE")
        self.radiobutton2.place(x=420,y=250)

        self.radiobutton3=Radiobutton(self.root,text="OTHERS",width=8,height=1,bg="#FFB6C1",activebackground="#fcfffd",font=('times new roman',11,'bold'),variable=self.radiobutton_value,value="OTHERS")
        self.radiobutton3.place(x=530,y=250)
        

        self.label6=Label(self.root,text="DOB",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label6.place(x=45,y=290)

        self.dob=DateEntry(self.root,date_pattern='yyyy/mm/dd',maxdate=date.today(),width=30)
        self.dob.place(x=310,y=290)
        

        self.label7=Label(self.root,text="WEIGHT IN KG ",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label7.place(x=45,y=330)
        
        self.wt_box=Entry(self.root,font=('times new roman',14,'bold'),bg="#FFB6C1")
        self.wt_box.place(x=310,y=330)

        self.label8=Label(self.root,text="HEIGHT IN  CENTIMETRES",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label8.place(x=45,y=370)

        self.ht_box=Entry(self.root,font=('times new roamn',14,'bold'),bg="#FFB6C1",width=18)
        self.ht_box.place(x=310,y=370)

        self.label9=Label(self.root,text="PHONE NUMBER",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label9.place(x=45,y=410)

        self.ph_box=Entry (self.root,font=('times new roman',14,'bold'),bg="#FFB6C1")
        self.ph_box.place(x=310,y=410)

        
        self.label10=Label(self.root,text="UPLOAD YOUR PHOTO",bg="#fcfffd",font=('times new roman',14,'bold'))
        self.label10.place(x=45,y=450)

        self.but1=Button(self.root,text="UPLOAD",font=('times new roman',14,'bold'),bd=2,relief='solid',bg="#FFB6C1",command=self.upload_file)
        self.but1.place(x=310,y=450)
        # self.img_label_display=Label(self.root,image=self.imgi_tk,bg="white")
        # self.img_label_display.place(x=1030,y=80)


        self.but2=Button(self.root,text="SUBMIT",font=('times new roman',14,'bold'),height=1,bd=2, relief="solid",bg="#FFB6C1",command=self.getval)
        self.but2.place(x=930,y=490)

        self.imgback=Image.open('back.jpg')
        self.imgback_new=self.imgback.resize((30,30))
        self.imgback_tk=ImageTk.PhotoImage(self.imgback_new)
        self.back_button=Button(self.root, text="BACK",image=self.imgback_tk,command=self.back,bg="white",bd=2,relief="solid")
        self.back_button.place(x=0,y=0)

        

        

        self.root.mainloop()
        # uploading and saving image in database
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
            
                
                self.img1_label.config(image=self.imgii_tk)
                self.img1_label.image= self.imgii_tk
        
            except Exception as e:
            # Show an error message if something goes wrong
                messagebox.showerror("Error", f"Failed to upload file: {str(e)}")
        else:
            messagebox.showwarning("No File", "No file was selected.")

        

    def getval(self):
        data=(self.name_entry.get(),self.age_box.get(),self.email_box.get(),self.pas_box.get(),self.radiobutton_value.get(),self.dob.get(),self.wt_box.get(),self.ht_box.get(),self.ph_box.get(),self.target_file_path)
    
        res=database.registerUser(data)
        if res:
            messagebox.showinfo("Database","User Registered Successfully")
            self.root.destroy()
            userlogin.login()
            
        else:
            messagebox.showerror("Error","Not Registered")
    def back(self):
        self.root.destroy()
        userpanel.user()
        
    def next_screen(self):
        self.root.destroy()
        dashboard_user.userboard()

    
    
    

if __name__=="__main__":
    register()

            



        



        




        


                             

        

        











        
                          





    