from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from f_r import f_d
from attendencs import atd
from train import Train
import os
from devloper import Devloper

from tkinter import messagebox

class Face_Recognition_System:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        

       
        # Background image
        img3 = Image.open(r"college_images/BestFacialRecognition.jpg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=0, y=130, width=1530, height=710)

        # add title
        tital_lbl=Label(f_lbl3,text="FACE RECOGNITION STTENDENCE SYSTEM SOFTWARE",font=("times new roman",32,"bold"),bg="white",fg="red")
        tital_lbl.place(x=0,y=0,width=1530,height=45)

        # student button
        img4 = Image.open(r"college_images/gettyimages-1022573162.jpg")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(f_lbl3,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=220)

        b1_1 = Button(f_lbl3,text="student Details",command=self.student_details,cursor="hand2")
        b1_1.place(x=100,y=300,width=220,height=40)

        # detectface button
        img5 = Image.open(r"college_images/face_detector1.jpg")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1 = Button(f_lbl3,image=self.photoimg5,cursor="hand2",command=self.face_d)
        b1.place(x=400,y=100,width=220,height=220)

        b1_1 = Button(f_lbl3,text="Face Detector",cursor="hand2",command=self.face_d)
        b1_1.place(x=400,y=300,width=220,height=40)

        #Attendanc button
        img6 = Image.open(r"college_images/report.jpg")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1 = Button(f_lbl3,image=self.photoimg6,cursor="hand2",command=self.attendence)
        b1.place(x=700,y=100,width=220,height=220)

        b1_1 = Button(f_lbl3,text="Attendance",cursor="hand2",command=self.attendence)
        b1_1.place(x=700,y=300,width=220,height=40)
      
        #help
        img7 = Image.open(r"college_images/help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1 = Button(f_lbl3,image=self.photoimg7,cursor="hand2")
        b1.place(x=1000,y=100,width=220,height=220)

        b1_1 = Button(f_lbl3,text="Help",cursor="hand2")
        b1_1.place(x=1000,y=300,width=220,height=40)

        #train
        img8 = Image.open(r"college_images/Train.jpg")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1 = Button(f_lbl3,image=self.photoimg8,cursor="hand2",command=self.train)
        b1.place(x=160,y=360,width=220,height=220)

        b1_1 = Button(f_lbl3,text="Train Data",cursor="hand2",command=self.train)
        b1_1.place(x=160,y=500,width=220,height=40)

        #photo
        img9 = Image.open(r"college_images/opencv_face_reco_more_data.jpg")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1 = Button(f_lbl3,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=450,y=360,width=220,height=220)

        b1_1 = Button(f_lbl3,text="Photo",cursor="hand2",command=self.open_img)
        b1_1.place(x=450,y=500,width=220,height=40)

        #devloper
        img10 = Image.open(r"college_images/har.jpg")
        img10 = img10.resize((220, 220))
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1 = Button(f_lbl3,image=self.photoimg10,command=self.devp,cursor="hand2")
        b1.place(x=750,y=360,width=220,height=220)

        b1_1 = Button(f_lbl3,text="Devloper",command=self.devp,cursor="hand2")
        b1_1.place(x=750,y=500,width=220,height=40)

        #Exit
        img111 = Image.open(r"college_images/exit.jpg")
        img111 = img111.resize((220, 220))
        self.photoimg111 = ImageTk.PhotoImage(img111)
        
        b1 = Button(f_lbl3,image=self.photoimg111,command=self.exit_window,cursor="hand2")
        b1.place(x=1050,y=360,width=220,height=220)

        b1_1 = Button(f_lbl3,text="Devloper",command=self.exit_window,cursor="hand2",)
        b1_1.place(x=1050,y=500,width=220,height=40)

    

    def open_img(self):
        os.startfile("data")
    def exit_window(self):
        
        response = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
        if response:  
            self.root.destroy()  
   


      

    # ===============================function buttons==========================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_d(self):
        self.new_window=Toplevel(self.root)
        self.app=f_d(self.new_window)
    def attendence(self):
        self.new_window=Toplevel(self.root)
        self.app=atd(self.new_window)
    def devp(self):
        self.new_window=Toplevel(self.root)
        self.app=Devloper(self.new_window)
    
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
