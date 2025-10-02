from tkinter import *
from PIL import Image,ImageTk
import database
from tkinter import messagebox
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
        print(d)
        # self.label1=Label(self.root,text='UNDERWEIGHT',font=('times new roman',15,'bold'),bg="#F2D2BD",fg="#0a0a0a")
        # self.label1.place(x=60,y=140)
        self.label=Label(self.root,text=f"Diet plan for {name} is:", font=('times new roman','17','bold'),bg="#F2D2BD",fg="#0a0a0a")
        self.label.place(x=500,y=50)
        self.label1=Label(self.root,text=f"{d}",font=('times new roman','15','bold'),bg="#F2D2BD")
        self.label1.place(x=500,y=120)
        self.root.mainloop()
       
if __name__=="__main__":
    diet(res=121235)