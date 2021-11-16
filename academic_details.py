from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Academic_details:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Details")
        self.root.geometry("760x635+255+155")

        self.var_10year = StringVar()
        self.var_10board = StringVar()
        self.var_10Percent = StringVar()
        self.var_12year = StringVar()
        self.var_12board = StringVar()
        self.var_12Percent = StringVar()
        self.var_stream = StringVar()
        

        lebelframeleft = LabelFrame(self.root, bd =2, relief=RIDGE,text="Academic Datails",padx=2, font=("times new roman", 12,"bold"))
        lebelframeleft.place(x=5, y=5,width = 750, height=625)

        lbl_cust_ref = Label(lebelframeleft, text="10TH Board  ", font=("times new roman", 15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0, sticky=W)

        lbl_cust_ref = Label(lebelframeleft, text="Year  ", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=1,column=0, sticky=W)
        enty_ref = ttk.Entry(lebelframeleft,textvariable=self.var_10year,width=18, font=("times new roman", 13,"bold"))
        enty_ref.grid(row=1,column=1, sticky=W)

        lbl_cust_ref = Label(lebelframeleft, text="Board  ", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=2,column=0, sticky=W)
        enty_ref = ttk.Entry(lebelframeleft,textvariable=self.var_10board,width=18, font=("times new roman", 13,"bold"))
        enty_ref.grid(row=2,column=1, sticky=W)

        lbl_cust_ref = Label(lebelframeleft, text="Percentage (in %)  ", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=3,column=0, sticky=W)
        enty_ref = ttk.Entry(lebelframeleft,textvariable=self.var_10Percent,width=18, font=("times new roman", 13,"bold"))
        enty_ref.grid(row=3,column=1, sticky=W)

        lbl_cust_ref = Label(lebelframeleft, text="12TH Board  ", font=("times new roman", 15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=4,column=0, sticky=W)

        lbl_cust_ref = Label(lebelframeleft, text="Year  ", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=5,column=0, sticky=W)
        enty_ref = ttk.Entry(lebelframeleft,textvariable=self.var_12year,width=18, font=("times new roman", 13,"bold"))
        enty_ref.grid(row=5,column=1, sticky=W)

        lbl_cust_ref = Label(lebelframeleft, text="Board  ", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=6,column=0, sticky=W)
        enty_ref = ttk.Entry(lebelframeleft,textvariable=self.var_12board,width=18, font=("times new roman", 13,"bold"))
        enty_ref.grid(row=6,column=1, sticky=W)

        lbl_artist_name = Label(lebelframeleft, text="Stream  ", font=("times new roman", 15,"bold"),padx=2,pady=6)
        lbl_artist_name.grid(row=7,column=0, sticky=W)
        combo_search = ttk.Combobox(lebelframeleft,textvariable=self.var_stream, font=("times new roman", 15,"bold"), width=24, state="readonly" )        
        combo_search["value"] = ("Science","Arts","Commerce")
        combo_search.current(0)
        combo_search.grid(row=7,column=1,padx=2)

        lbl_cust_ref = Label(lebelframeleft, text="Percentage (in %)  ", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=8,column=0, sticky=W)
        enty_ref = ttk.Entry(lebelframeleft,textvariable=self.var_12Percent,width=18, font=("times new roman", 13,"bold"))
        enty_ref.grid(row=8,column=1, sticky=W)

        lebelframeDown = LabelFrame(lebelframeleft, bd =2, relief=RIDGE,text="scholarship criteria",padx=2, font=("times new roman", 12,"bold"))
        lebelframeDown.place(x=5, y=340,width = 730, height=160)

        lbl_cust_ref = Label(lebelframeDown, text="Scholarship Name : Freeship Scholarship  ", font=("times new roman", 15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0, sticky=W)

        lbl_cust_ref = Label(lebelframeDown, text="Require Percentage  ", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=1,column=0, sticky=W)
        lbl_cust_ref = Label(lebelframeDown, text="90.00", font=("times new roman", 15,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=1,column=1, sticky=W)
        

        lbl_cust_ref = Label(lebelframeDown, text="Actual Percentage  ", font=("times new roman", 12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=2,column=0, sticky=W)
        enty_ref = ttk.Entry(lebelframeDown,textvariable=self.var_12Percent,width=18, font=("times new roman", 13,"bold"))
        enty_ref.grid(row=2,column=1, sticky=W)    


        btn_frame = Frame(lebelframeleft,bd=2, relief=RIDGE)
        btn_frame.place(x=540, y=530, width=110,height=40)
        
        btnSUBMIT = Button(btn_frame,text="Finish",command=self.add_data,font=("times new roman", 13,"bold"), bg ="green",fg="white", width=9,padx=1, bd=5)
        btnSUBMIT.grid(row=0,column=0)
  

    def add_data(self):
        ssc_year = self.var_10year.get()
        ssc_board = self.var_10board.get()
        ssc_percent = self.var_10Percent.get()
        hsc_year = self.var_12year.get()
        hsc_board = self.var_12board.get()
        hsc_percent = self.var_12Percent.get()
        stream = self.var_stream.get()

        if ssc_year =='' or ssc_board=='' or ssc_percent == '' or hsc_year=='' or hsc_board=='' or hsc_percent=='' or stream=='':
            messagebox.showerror(
                "Error", "All Field Are Require", parent=self.root)
        else:            
            file = open('tool.txt','a')
            file.write(ssc_year + "\n")
            file.write(ssc_board + "\n")
            file.write(ssc_percent + "\n")
            file.write(hsc_year + "\n")
            file.write(hsc_board + "\n")
            file.write(hsc_percent + "\n")
            file.write(stream + "\n")
            file.close() 
            messagebox.showinfo(
                "Success", "Data Succesfully sent to Tool", parent=(self.root))


if __name__ == "__main__":
    root = Tk()
    obj = Academic_details(root)
    root.mainloop()