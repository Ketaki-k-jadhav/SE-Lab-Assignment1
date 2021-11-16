from tkinter import *
from personal_details import Personal_details
from academic_details import Academic_details
from test import tool_window	


class form:

	def __init__(self, root):
		self.root = root
		self.root.title("Scholarship Form")
		self.root.geometry("780x800+250+0")

		lbl_title = Label(self.root, text="Scholarship Form", font=("times new roman", 40,"bold"),bg= "white", fg="black",bd=4,relief=RIDGE)
		lbl_title.place(x=0, y=0, width=770, height=70)

		main_frame =Frame(self.root, bd=4, relief=RIDGE)
		main_frame.place(x=0,y=70,width=770,height=730)
		
		lbl_menu = Label(main_frame, text="DETAILS", font=("times new roman", 20, "bold"), bg="light yellow", fg="blue", bd=5, relief=RIDGE)
		lbl_menu.place(x=0, y=0, width=150)

		btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
		btn_frame.place(x=160, y=0, width=420)
		
		cust_btn = Button(btn_frame, text="Personal Details",command=self.personal_deatails, width=13, font=("times new roman", 17, "bold"),bg ="green",fg="white", bd=5, relief=RIDGE)
		cust_btn.grid(row=0, column=0, padx=2)
		
		arts_btn = Button(btn_frame, text="Academic Details",command=self.academic_deatails, width=13, font=("times new roman", 17, "bold"), bg ="green",fg="white", bd=5, relief=RIDGE)
		arts_btn.grid(row=0, column=1, padx=2)

		# tool_btn = Button(main_frame, text="Test",command=self.validation_deatails, width=5, font=("times new roman", 17, "bold"), bg ="green",fg="white", bd=5, relief=RIDGE)
		# tool_btn.place(x=600, y=0)
		# reset_btn = Button(main_frame, text="Reset",command=self.personal_deatails, width=4, font=("times new roman", 17, "bold"), bg ="green",fg="white", bd=5, relief=RIDGE)
		# reset_btn.place(x=690, y=0)

		lbl_body = Label(self.root, text="to add details click on Personal Details ", font=("times new roman", 12,"bold"),bg= "white", fg="black",bd=4,relief=RIDGE)
		lbl_body.place(x=180, y=260, width=400, height=70)
		
	def personal_deatails(self):
		self.new_window = Toplevel(self.root)
		self.app = Personal_details(self.new_window)
	
	def academic_deatails(self):
		self.new_window = Toplevel(self.root)
		self.app = Academic_details(self.new_window)

	def validation_deatails(self):
		self.new_window = Toplevel(self.root)
		self.app = tool_window(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = form(root)
    root.mainloop()
    