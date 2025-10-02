from tkinter import *
from PIL import Image,ImageTk
import database
from tkinter import messagebox
import dashboard_user
# from view_my_clients import save_plan
class diet:
    def __init__(self,res):
        self.res=res
        # self.id=id
        self.root=Tk()
        self.root.title("User Diet")
        self.width=self.root.winfo_screenwidth()-100
        self.height=self.root.winfo_screenheight()-100

        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False,False)

        self.image1=Image.open('diet1.jpeg')
        self.image1_new=self.image1.resize((self.width,self.height))
        self.image1_tk=ImageTk.PhotoImage(image=self.image1_new)
        self.image1.label=Label(self.root,image=self.image1_tk)
        self.image1.label.place(x=0,y=0)

        self.frame1=Frame(self.root,bg="#fff2d7",width=700,height=583)
        self.frame1.place(x=480,y=30)
        # self.fetch_clients()
        
        name=res[1]
        id=res[0]
        d=database.getdiet(id)
        # print(d)
       
        self.label=Label(self.root,text=f"Diet plan for {name} is:", font=('times new roman','17','bold'),bg="#fff2d7",fg="#0a0a0a")
        self.label.place(x=400,y=40)
        self.label1=Label(self.root,text=f"{d}",font=('times new roman','15','bold'),bg="#fff2d7")
        self.label1.place(x=600,y=80)
        
        self.imgback=Image.open('back.jpg')
        self.imgback_new=self.imgback.resize((30,30))
        self.imgback_tk=ImageTk.PhotoImage(self.imgback_new)
        self.back_button=Button(self.root, text="BACK",image=self.imgback_tk,bg="white",bd=2,relief="solid",command=self.back)
        self.back_button.place(x=0,y=0)
        self.root.mainloop()
    def back(self):
        self.root.destroy()
        dashboard_user.userboard(self.res)

    
if __name__=="__main__":
    diet(res=121235)