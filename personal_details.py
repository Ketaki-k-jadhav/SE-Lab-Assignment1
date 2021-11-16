from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random


class Personal_details:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Details")
        self.root.geometry("760x635+255+155")

        self.var_ref = StringVar()
        x = random.randint(10000, 99999)
        self.var_ref.set(str(x))

        self.var_name = StringVar()
        self.var_bd = StringVar()
        self.var_age = StringVar()
        self.var_email = StringVar()
        self.var_addr = StringVar()
        self.var_mono = StringVar()
        self.var_gid = StringVar()
        self.var_gender = StringVar()
        self.var_adhaar = StringVar()
        self.var_bankname = StringVar()
        self.var_branch = StringVar()
        self.var_ifsc = StringVar()
        self.var_acno = StringVar()

        self.var_name.set(""),
        self.var_bd.set(""),
        self.var_age.set(""),
        self.var_email.set(""),
        self.var_addr.set(""),
        self.var_mono.set(""),
        self.var_gid.set(""),
        self.var_gender.set(""),
        self.var_adhaar.set(""),
        self.var_bankname.set(""),
        self.var_branch.set(""),
        self.var_ifsc.set(""),
        self.var_acno.set("")

        lebelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Personal Datails", padx=2, font=(
            "times new roman", 12, "bold"))
        lebelframeleft.place(x=5, y=5, width=750, height=625)

        lbl_cust_ref = Label(lebelframeleft, text="Student Information  ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        lbl_cust_ref = Label(lebelframeleft, text="Reference ID  ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=1, column=0, sticky=W)
        enty_ref = ttk.Entry(lebelframeleft, width=30, textvariable=self.var_ref, font=(
            "times new roman", 12, "bold"), state="readonly")
        enty_ref.grid(row=1, column=1, sticky=W)

        lbl_cust_ref = Label(lebelframeleft, text="Full Name  ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=2, column=0, sticky=W)
        enty_ref = ttk.Entry(lebelframeleft, width=30, textvariable=self.var_name, font=(
            "times new roman", 15, "bold"))
        enty_ref.grid(row=2, column=1, sticky=W)

        lbl_artist_name = Label(lebelframeleft, text="Birth Date  ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_artist_name.grid(row=3, column=0, sticky=W)
        enty_name = ttk.Entry(lebelframeleft, textvariable=self.var_bd, width=29, font=(
            "times new roman", 12, "bold"))
        enty_name.grid(row=3, column=1)

        lbl_artist_name = Label(lebelframeleft, text="Age  ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_artist_name.grid(row=4, column=0, sticky=W)
        enty_name = ttk.Entry(lebelframeleft, textvariable=self.var_age, width=29, font=(
            "times new roman", 12, "bold"))
        enty_name.grid(row=4, column=1)

        lbl_artist_name = Label(lebelframeleft, text="Mobile No  ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_artist_name.grid(row=5, column=0, sticky=W)
        enty_name = ttk.Entry(lebelframeleft, textvariable=self.var_mono, width=29, font=(
            "times new roman", 12, "bold"))
        enty_name.grid(row=5, column=1)

        lbl_artist_name = Label(lebelframeleft, text="Email Address ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_artist_name.grid(row=6, column=0, sticky=W)
        enty_name = ttk.Entry(lebelframeleft, textvariable=self.var_email, width=29, font=(
            "times new roman", 12, "bold"))
        enty_name.grid(row=6, column=1)

        lbl_artist_name = Label(lebelframeleft, text="Home Address  ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_artist_name.grid(row=7, column=0, sticky=W)
        enty_name = ttk.Entry(lebelframeleft, width=29, textvariable=self.var_addr, font=(
            "times new roman", 12, "bold"))
        enty_name.grid(row=7, column=1)

        lbl_artist_name = Label(lebelframeleft, text="Gender  ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_artist_name.grid(row=8, column=0, sticky=W)
        combo_search = ttk.Combobox(lebelframeleft, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Male", "Female", "Other")
        combo_search.current(0)
        combo_search.grid(row=8, column=1, padx=2)

        lebelframeDown = LabelFrame(lebelframeleft, bd=2, relief=RIDGE,
                                    text="Bank Details", padx=2, font=("times new roman", 12, "bold"))
        lebelframeDown.place(x=5, y=330, width=730, height=215)

        lbl_artist_name = Label(lebelframeDown, text="Adhaar Number  ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_artist_name.grid(row=10, column=0, sticky=W)
        enty_name = ttk.Entry(lebelframeDown, textvariable=self.var_adhaar, width=29, font=(
            "times new roman", 12, "bold"))
        enty_name.grid(row=10, column=1)

        lbl_artist_name = Label(lebelframeDown, text="Bank Name  ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_artist_name.grid(row=11, column=0, sticky=W)
        enty_name = ttk.Entry(lebelframeDown, textvariable=self.var_bankname, width=29, font=(
            "times new roman", 15, "bold"))
        enty_name.grid(row=11, column=1)

        lbl_artist_name = Label(lebelframeDown, text="Branch  ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_artist_name.grid(row=12, column=0, sticky=W)
        enty_name = ttk.Entry(lebelframeDown, textvariable=self.var_branch, width=29, font=(
            "times new roman", 12, "bold"))
        enty_name.grid(row=12, column=1)

        lbl_artist_name = Label(lebelframeDown, text="IFSC Code  ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_artist_name.grid(row=13, column=0, sticky=W)
        enty_name = ttk.Entry(lebelframeDown, textvariable=self.var_ifsc, width=29, font=(
            "times new roman", 12, "bold"))
        enty_name.grid(row=13, column=1)

        lbl_artist_name = Label(lebelframeDown, text="Acount Number  ", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_artist_name.grid(row=14, column=0, sticky=W)
        enty_name = ttk.Entry(lebelframeDown, textvariable=self.var_acno, width=29, font=(
            "times new roman", 12, "bold"))
        enty_name.grid(row=14, column=1)

        btn_frame = Frame(lebelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=540, y=555, width=110, height=40)

        btnSUBMIT = Button(btn_frame, text="Next", command=self.add_data, font=(
            "times new roman", 13, "bold"), bg="green", fg="white", width=9, padx=1, bd=5)
        btnSUBMIT.grid(row=0, column=0)

    def add_data(self):
        ref_no = self.var_ref.get()
        name = self.var_name.get()
        birth_date = self.var_bd.get()
        age = self.var_age.get()
        mobileno = self.var_mono.get()
        email = self.var_email.get()
        addr = self.var_addr.get()
        gender = self.var_gender.get()
        adhaar = self.var_adhaar.get()
        bankname = self.var_bankname.get()
        branch = self.var_branch.get()
        ifsc = self.var_ifsc.get()
        acount = self.var_acno.get()

        if ref_no == '' or name == '' or birth_date == '' or age == '' or mobileno == '' or email == '' or addr == '' or gender == '' or adhaar == '' or bankname == '' or branch == '' or ifsc == '' or acount == '':
            messagebox.showerror(
                "Error", "All Field Are Require", parent=self.root)
        else:
            file = open('tool.txt', 'w')
            file.write(ref_no + "\n")
            file.write(name + "\n")
            file.write(birth_date + "\n")
            file.write(age + "\n")
            file.write(mobileno + "\n")
            file.write(email + "\n")
            file.write(addr + "\n")
            file.write(gender + "\n")
            file.write(adhaar + "\n")
            file.write(bankname + "\n")
            file.write(branch + "\n")
            file.write(ifsc + "\n")
            file.write(acount + "\n")
            file.close()
            messagebox.showinfo(
                "Success", "Data Succesfully sent to Tool", parent=(self.root))


if __name__ == "__main__":
    root = Tk()
    obj = Personal_details(root)
    root.mainloop()
