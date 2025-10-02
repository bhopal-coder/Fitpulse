from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import dashboard_trainer
from tkinter import messagebox
import database  # Assuming database is the module handling DB operations

class ViewMyClients:
    def __init__(self, trainer_id,res):
        self.res=res
        self.trainer_id = trainer_id
        self.root = tk.Tk()
        self.root.title("Client Details")
        # self.width = self.root.winfo_screenwidth() - 900
        self.width = self.root.winfo_screenwidth() - 100
        self.height = self.root.winfo_screenheight() - 100
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(True, True)  # Allow resizing

        
        # Heading
        self.heading = tk.Label(self.root, text="My Clients", font=('Arial', 24, 'bold'))
        self.heading.pack(pady=20)

        # Create a canvas to hold the client cards
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill="both", expand=True, side=tk.LEFT)

        self.img_bg1=Image.open('pastel orange3.jpg')
        self.img_bg_new1=self.img_bg1.resize((self.width,self.height))
        self.img_bg_tk1=ImageTk.PhotoImage(self.img_bg_new1)
        self.img_bg_label1=Label(self.canvas,image=self.img_bg_tk1)
        self.img_bg_label1.place(x=0,y=0)

        # Add a scrollbar to the canvas
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.card_frame = tk.Frame(self.canvas, bg="#f0f0f0")
        self.canvas.create_window((0, 0), window=self.card_frame, anchor="nw")
        self.img_bg=Image.open('pastel orange3.jpg')
        self.img_bg_new=self.img_bg.resize((self.width,self.height))
        self.img_bg_tk=ImageTk.PhotoImage(self.img_bg_new)
        self.img_bg_label=Label(self.card_frame,image=self.img_bg_tk)
        self.img_bg_label.place(x=0,y=0)

        self.fetch_clients()
        
        self.root.mainloop()

    def fetch_clients(self):
        clients = database.query_clients_for_trainer(self.trainer_id)
        print(clients)

        # Create a card for each client
        for client in clients:
            self.create_client_card(client)

    def create_client_card(self, client):
        # Card frame
        card = tk.Frame(self.card_frame, bg="#f0f0f0", bd=2, relief="raised", padx=10, pady=10)
        card.pack(fill="x", padx=400, pady=15)
        # card.pack(fill='x')
        # name=client[1]
        id=client[0]
        d=database.getbmi(id)
        if d<18.5:
            cate='Underweight'
        elif d>=18.5 and d<=24.9:
            cate='Normal Weight'
        elif d>=25 and d<=29.9:
            cate='Overweight'
        elif d>=30 and d<=34.9:
            cate='Obesity'
        elif d>35:
            cate='Extremely Obese'
        else:
            cate=None
        # Client photo
        image_path = client[6]  # Assuming client[6] contains the path to the client's photo
        image = Image.open(image_path)
        image = image.resize((120, 120))
        photo = ImageTk.PhotoImage(image)

        photo_label = tk.Label(card, image=photo)
        photo_label.image = photo  # Keep a reference to avoid garbage collection
        photo_label.pack(side=tk.LEFT, padx=10)

        # Client details
        details_frame = tk.Frame(card, bg="#f0f0f0")
        details_frame.pack(side=tk.LEFT, padx=20)

        name_label = tk.Label(details_frame, text=f"Name: {client[1]}", font=('Arial', 16, 'bold'), bg="#f0f0f0")
        name_label.pack(anchor="w")

        email_label = tk.Label(details_frame, text=f"Email: {client[2]}", font=('Arial', 14), bg="#f0f0f0")
        email_label.pack(anchor="w")

        phone_label = tk.Label(details_frame, text=f"Phone: {client[3]}", font=('Arial', 14), bg="#f0f0f0")
        phone_label.pack(anchor="w")

        weight_label = tk.Label(details_frame, text=f"Weight: {client[4]} kg", font=('Arial', 14), bg="#f0f0f0")
        weight_label.pack(anchor="w")

        height_label = tk.Label(details_frame, text=f"Height: {client[5]} cm", font=('Arial', 14), bg="#f0f0f0")
        height_label.pack(anchor="w")

        bmi_label=tk.Label(details_frame, text=f"BMI: {d}cm, {cate}", font=('Arial', 14), bg="#f0f0f0")
        bmi_label.pack(anchor="w")
        

        # Buttons to add diet and workout plans
        button_frame = tk.Frame(card, bg="#f0f0f0")
        button_frame.pack(side=tk.RIGHT, padx=20)

        diet_button = tk.Button(button_frame, text="Add Diet Plan", command=lambda: self.add_diet_plan(client[0]))
        diet_button.pack(pady=5)

        # workout_button = tk.Button(button_frame, text="Add Workout Plan", command=lambda: self.add_workout_plan(client[0]))
        # workout_button.pack(pady=5)
        self.imgback=Image.open('back.jpg')
        self.imgback_new=self.imgback.resize((30,30))
        self.imgback_tk=ImageTk.PhotoImage(self.imgback_new)
        self.back_button=Button(self.root, text="BACK",image=self.imgback_tk,bg="black",bd=2,relief="solid",command=self.back)
        self.back_button.place(x=10,y=10)

        # print(client) 

    def add_diet_plan(self, client_id):
        self.new_window("Diet Plan", client_id)

    def new_window(self, title, client_id):
        new_win = tk.Toplevel(self.root)
        new_win.title(f"Add {title}")
        new_win.geometry(f"{self.width}x{self.height}")

        label = tk.Label(new_win, text=f"Add {title} for Client ID: {client_id}", font=('Arial', 16, 'bold'))
        label.pack(pady=20)

        # Text area for adding plan details
        text_area = tk.Text(new_win, width=50, height=10)
        text_area.pack(pady=10)

        # Save button
        save_button = tk.Button(new_win, text="Save", command=lambda: self.save_plan(client_id, title, text_area.get("1.0", "end-1c")))
        save_button.pack(pady=70)
       
        
        
        
    def save_plan(self, client_id, title, plan_text):
        data=(title,plan_text)
        id=client_id
        print(data)                        
        res=database.diet(data,id)
        if res:
            messagebox.showinfo("Success","Diet suggested successfully!")
           
        else:
            messagebox.showerror("Error","Diet Not suggested!")

        return data
    
    def back(self):
        self.root.destroy()
        dashboard_trainer.trainerboard(self.res) 

    # def back_newwindow(self):
    #     self.root.destroy()
    #     dashboard_trainer.trainerboard(self.res) 
                                            
if __name__ == "__main__":
    ViewMyClients(trainer_id=5)  
