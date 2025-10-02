import tkinter as tk
from tkinter import *
from tkcalendar import dateentry
from tkinter import BOTH  
import view_customers
import view_trainers
import add_assign
import view_assign
import first_screen

class home_screen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600")
        self.root.title('Fitpulse')      
        self.root.resizable(False, False)


        options_frame = tk.Frame(self.root, bg="#2b3030", width=300)
        self.home_btn = tk.Button(options_frame, text='Home', font=('Bold', 15),
                                  fg='white', bd=0, bg='#2b3030', command=lambda: self.indicate(self.home_indicate, self.showall))
        self.home_btn.place(x=10, y=70)
        self.home_indicate = tk.Label(options_frame, text="", bg="white")
        self.home_indicate.place(x=3, y=70, width=5, height=40)
        self.emp_list = tk.Button(options_frame, text='Manage Trainers', font=('Bold', 14),
                                  fg='white', bd=0, bg='#2b3030', command=lambda: self.indicate(self.emp_indicate, self.showalltrainers))
        self.emp_list.place(x=10, y=120)
        self.emp_indicate = tk.Label(options_frame, text="", bg="#2b3030")
        self.emp_indicate.place(x=3, y=120, width=5, height=40)


        self.pending_user = tk.Button(options_frame, text='Manage User', font=('Bold', 15),
                                      fg='white', bd=0, bg='#2b3030', command=lambda: self.indicate(self.user_indicate, self.showallUser))
        self.pending_user.place(x=10, y=170)
        self.user_indicate = tk.Label(options_frame, text="", bg="#2b3030")
        self.user_indicate.place(x=3, y=170, width=5, height=40)
        
        
        self.pro_list = tk.Button(options_frame, text='Assign Trainers', font=('Bold', 14),
                                  fg='white', bd=0, bg='#2b3030', command=lambda: self.indicate(self.emp_indicate, self.assignTrainers))
        self.pro_list.place(x=10, y=220)
        self.pro_indicate = tk.Label(options_frame, text="", bg="#2b3030")
        self.pro_indicate.place(x=3, y=220, width=5, height=40)

        self.man_pro = tk.Button(options_frame, text='View Assign Trainers', font=('Bold', 15),
                                      fg='white', bd=0, bg='#2b3030', command=lambda: self.indicate(self.user_indicate, self.viewassignTrainers))
        self.man_pro.place(x=10, y=270)
        self.man_pro_indicate = tk.Label(options_frame, text="", bg="#2b3030")
        self.man_pro_indicate.place(x=3, y=270, width=5, height=40)



       

        options_frame.pack(side=tk.LEFT)
        options_frame.pack_propagate(False)
        options_frame.configure(width=210, height=600)
        

        self.main_frame = tk.Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=750, height=600)

        # Show user list frame on startup
        # self.userlist()
        self.home_indicate.config(bg="white")
        self.showall()
        self.button8=Button(self.root,text="LogOut",font=('Times new roman',15,'bold'),bg="#0a0a0a",bd=1,relief="solid",fg="#fcfffd",command=self.logout)
        self.button8.place(x=20,y=30)
        self.root.mainloop()

    def indicate(self, lb, page):
        self.hide_indicators()
        lb.config(bg="white")
        self.delete_frame()
        page()

    def hide_indicators(self):
        self.home_indicate.config(bg="#2b3030")
        self.emp_indicate.config(bg="#2b3030")
        self.user_indicate.config(bg="#2b3030")
        # self.task_indicate.config(bg="#2b3030")
    def logout(self):
        self.root.destroy()
        first_screen.welcome()

    def showall(self):
        pass
    def showalltrainers(self):
        obj=view_trainers.ViewTrainer(self.main_frame)
        obj.manageTrainer()
        
    def showallUser(self):
        obj=view_customers.ViewCustomer(self.main_frame)
        obj.manageCustomer()

    def assignTrainers(self):
        obj= add_assign.createAdd(self.main_frame)
        obj.firstFrame()
        
    def viewassignTrainers(self):
        obj= view_assign.viewAssignTask(self.main_frame)
        obj.manageTask()

    
    # def task_list(self):
    #     task_frame = tk.Frame(self.main_frame)
    #     lb = tk.Label(task_frame, text="Task List yet to implement", font=("bold", 20))
    #     lb.pack()
    #     task_frame.pack(pady=20)

    def delete_frame(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

if __name__ == "__main__":
    home_screen()
