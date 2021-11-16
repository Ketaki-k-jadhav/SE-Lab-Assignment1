import sys
import re
from datetime import *
from tkinter import *
from tkinter import messagebox


class Test():
    
    def __init__(self,input_file):
        self.test_file=open("testing_output.txt","w")
        try:
            f=open(input_file,"r")
            print("Successfully opened the input file\n")
        except:
            print("Unable to open input file\n")
            sys.exit()

        self.required_hsc_percentage = 90.0
        self.id = f.readline()[:-1]
        self.name = f.readline()[:-1]
        self.dob = f.readline()[:-1]
        self.age = f.readline()[:-1]
        self.mob_number = f.readline()[:-1]
        self.email = f.readline()[:-1]
        self.address = f.readline()[:-1]
        self.gender = f.readline()[:-1]

        self.aadhar = f.readline()[:-1]
        self.bank_name = f.readline()[:-1]
        self.branch = f.readline()[:-1]
        self.ifsc_code = f.readline()[:-1]
        self.account_number = f.readline()[:-1]

        self.ssc_year = f.readline()[:-1]
        self.ssc_board = f.readline()[:-1]
        self.ssc_percentage = f.readline()[:-1]

        self.hsc_year = f.readline()[:-1]
        self.hsc_board = f.readline()[:-1]
        self.hsc_percentage = f.readline()[:-1]
        self.hsc_stream = f.readline()[:-1]

    def test_case1(self):
        name = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if(name.search(self.name) != None) or (any(chr.isdigit() for chr in self.name)):
            self.test_file.write(
                "Name is invalid...contains special characters/numbers\n")

    def test_case2(self):
        try:
            datetime.strptime(self.dob, "%d/%m/%Y")
        except:
            self.test_file.write(
                "Date of birth is not in DD/MM/YYYY format or incorrect date is entered\n")

    def test_case3(self):
        current_year = date.today().year
        birthdate = datetime.strptime(self.dob, "%d/%m/%Y")
        birth_year = birthdate.year
        age = current_year-birth_year
        if birth_year >=current_year:
            self.test_file.write("Year of birth is wrong\n")
        if(int(self.age) != age):
            self.test_file.write(
                "Age is incorrect given the entered date of birth\n")

    def test_case4(self):
        length = len(self.mob_number)
        if(length == 10 and self.mob_number.isdigit()):
            output = re.findall(r"^[789]\d{9}$", self.mob_number)
            if(len(output) != 1):
               self.test_file.write("Invalid Mobile number\n")
        else:
            self.test_file.write("Invalid Mobile number\n")

    def test_case5(self):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(email_regex, self.email)):
            self.test_file.write("Invalid email address\n")

    def test_case6(self):
        length = len(self.aadhar)
        if(length != 12 or not self.aadhar.isdigit()):
            self.test_file.write("Invalid aadhar number\n")

    def test_case7(self):
        str = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if(str.search(self.bank_name) != None) or (any(chr.isdigit() for chr in self.bank_name)):
            self.test_file.write("Name of the bank is not valid\n")
        if(str.search(self.branch) != None) or (any(chr.isdigit() for chr in self.branch)):
            self.test_file.write("Name of the bank branch is not valid\n")

    def test_case8(self):
        length = len(self.ifsc_code)
        if length != 11:
            self.test_file.write("Invalid IFSC code\n")
            return
        chars = self.ifsc_code[0:4]
        reserved = self.ifsc_code[4]
        digits = self.ifsc_code[5:]
        if(reserved != "0" and not digits.isdigit() and not chars.isalpha()):
            self.test_file.write("Invalid IFSC code\n")

    def test_case9(self):
        length = len(self.account_number)
        if not (9 <= length <= 18 and self.account_number.isdigit()):
            self.test_file.write("Invalid bank account number\n")

    def test_case10(self):
        current_year = date.today().year
        if len(self.ssc_year)!=4 or not self.ssc_year.isdigit() or int(self.ssc_year)>current_year:
            self.test_file.write("SSC Year of examination is not valid\n")
        if float(self.ssc_percentage) < 0.0 or float(self.ssc_percentage) > 100.0:
            self.test_file.write("SSC percentage is not valid\n")

    def test_case11(self):
        current_year = date.today().year
        if len(self.hsc_year)!=4 or not self.hsc_year.isdigit() or int(self.hsc_year)>current_year:
            self.test_file.write("HSC Year of examination is not valid\n")
        if float(self.hsc_percentage) < 0.0 or float(self.hsc_percentage) > 100.0:
            self.test_file.write("HSC percentage is not valid\n")

    def is_eligible(self):
        if(float(self.hsc_percentage) >= self.required_hsc_percentage):
            pass
        else:
            self.test_file.write(
                "\nYou are NOT ELIGIBLE for this scholarship\n")

def tool():
    filename="tool.txt"   
    info=Test(filename)
    info.test_case1()
    info.test_case2()
    info.test_case3()
    info.test_case4()
    info.test_case5()
    info.test_case6()
    info.test_case7()
    info.test_case8()
    info.test_case9()
    info.test_case10()
    info.test_case11()
    info.is_eligible()

class tool_window:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Validation Details")
        self.root.geometry("760x635+255+155")

        self.data = StringVar()

        lebelframeleft = LabelFrame(self.root, bd =2, relief=RIDGE,text="Validation Datails",padx=2, font=("times new roman", 12,"bold"))
        lebelframeleft.place(x=5, y=5,width = 750, height=625)

        with open("testing_output.txt", "r") as file:
            self.data = file.readlines()
            i=0
            for line in self.data:
                lbl_cust_ref = Label(lebelframeleft, text=line, font=("times new roman", 15,"bold"),padx=2,pady=6)
                lbl_cust_ref.grid(row=i,column=0, sticky=W)
                i=i+1
               
        if self.data == []:
            messagebox.showinfo(
                "Success", "You are Eligible !!", parent=(self.root))
        else:
            messagebox.showerror(
                "Error", "Please Refill Form Or Please check your Eligibility", parent=self.root)    
    


if __name__ == "__main__":
    tool()
    root = Tk()
    obj = tool_window(root)
    root.mainloop()
