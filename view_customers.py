from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import database


class ViewCustomer():
    # constructor
    def __init__(self, window):
        self.root = window
    
        
    def manageCustomer(self):
        self.fr = Frame(self.root, bg="light blue")
        self.fr.place(x=0, y=0, width="800", height="500")

        self.tr = Treeview(self.fr, columns=('K','A', 'B', 'C', 'E', 'F', 'G','H', 'I','J','M','L'), selectmode="extended")


        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=0, width=40, stretch=NO)

        self.tr.heading('#1', text="Name")
        self.tr.column('#1', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#2', text="Age")
        self.tr.column('#2', minwidth=0, width=30, stretch=NO)

        self.tr.heading('#3', text="Email")
        self.tr.column('#3', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#4', text="Password")
        self.tr.column('#4', minwidth=0, width=60, stretch=NO)

        self.tr.heading('#5', text="Gender")
        self.tr.column('#5', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#6', text="DOB")
        self.tr.column('#6', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#7', text="Weight")
        self.tr.column('#7', minwidth=0, width=50, stretch=NO)
        
        self.tr.heading('#8', text="Height")
        self.tr.column('#8', minwidth=0, width=50, stretch=NO)
        
        self.tr.heading('#9', text="Contact.")
        self.tr.column('#9', minwidth=0, width=80, stretch=NO)


        self.tr.heading('#10', text="Delete")
        self.tr.column('#10', minwidth=0, width=60, stretch=NO)

        data = database.getAllUser()
        print(data)
        for i in data:
            self.tr.insert('', 0, text = i[0], values=(i[1], i[2], i[3], i[4], i[5],i[6],
             str(i[7]),i[8],i[9],  'Delete'))



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
        if col == '#8':
            response = messagebox.askyesno('Delete','Do you really want to delete?')
            if response:
                a = database.deleteUser(gup)
                if a:
                    messagebox.showinfo('Success', 'User deleted successfully.')
                    obj = ViewCustomer(self.root)
                    obj.manageTrainer()
                else:
                    messagebox.showinfo('Alert', 'Something went wrong.')
        # if col =="#8":
            # obj = editemployee.createEditEmployee(self.root)
            # obj.firstFrame(gup)



if __name__ == '__main__':
    obj = ViewCustomer()
    obj.manageCustomer()
        
            