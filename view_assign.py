from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import database


class viewAssignTask():
    # constructor
    def __init__(self, window):
        self.root = window
        
    def manageTask(self):
        self.fr = Frame(self.root, bg="Grey")
        self.fr.place(x=0, y=0, width="800", height="500")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F'), selectmode="extended")

        self.tr.heading('#0', text="Id")
        self.tr.column('#0', minwidth=0, width=60, stretch=NO)

        self.tr.heading('#1', text="Customer Id")
        self.tr.column('#1', minwidth=0, width=120, stretch=NO)

        self.tr.heading('#2', text="Trainer Id")
        self.tr.column('#2', minwidth=0, width=120, stretch=NO)

        # self.tr.heading('#3', text="Start Date")
        # self.tr.column('#3', minwidth=0, width=80, stretch=NO)

        # self.tr.heading('#4', text="End Date")
        # self.tr.column('#4', minwidth=0, width=80, stretch=NO)

        # self.tr.heading('#5', text="Status")
        # self.tr.column('#5', minwidth=0, width=80, stretch=NO)
        
        self.tr.heading('#3', text="Edit")
        self.tr.column('#3', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#4', text="Delete")
        self.tr.column('#4', minwidth=0, width=80, stretch=NO)

        data = database.allassignTrainer()
        print(data)
        for i in data:
            self.tr.insert('', 0, text = i[0], values=(i[1], i[2], 'Edit', 'Delete'))



            
      
        # create double action button
        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0, y=0,height=500,width=800)
        self.root.mainloop()
    


    def actions(self, e):
        # get the values of the selected rows\\
        tt = self.tr.focus()

        # get the column id
        col = self.tr.identify_column(e.x)
        print(col)
        print(self.tr.item(tt))

        gup = (
            self.tr.item(tt).get('text'),
        )
        print(gup)
       
        if col == '#4':
            response = messagebox.askyesno('Delete','Do you really want to delete?')
            if response:
                a = database.deleteAssign(gup)
                if a:
                    messagebox.showinfo('Success', 'Deleted successfully.')
                    obj = viewAssignTask(self.root)
                    obj.manageTask()
                else:
                    messagebox.showinfo('Alert', 'Something went wrong.')

        if col =="#6":
            self.root.destroy()
            # obj = editassigntask.createAssignTask()
            # obj.firstFrame(gup)




if __name__ == '__main__':
    obj = viewAssignTask()
    obj.manageTask()
        
            