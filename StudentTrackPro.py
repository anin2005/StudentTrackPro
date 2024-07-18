import tkinter as tk
from tkinter import ttk
import pymysql

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Management System")

title_label = tk.Label(win, text="Student Management System", font=("Arial", 30, "bold"), border=12, relief=tk.GROOVE)
title_label.pack(side=tk.TOP, fill=tk.X)

detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Arial", 20))
detail_frame.place(x=20, y=90, width=420, height=575)

data_frame = tk.Frame(win, bd=12, bg="Lightgrey", relief=tk.GROOVE)
data_frame.place(x=475, y=90, width=810, height=575)

#============== Variables ===============#

rollno = tk.StringVar()
name = tk.StringVar()
class_ = tk.StringVar()
section = tk.StringVar()
contact = tk.StringVar()
fathers_name = tk.StringVar()
address = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()

#========= ENTRY =============#

rollno_lbl = tk.Label(detail_frame, text="Roll No ", font=('Arial', 15), bg="lightgrey")
rollno_lbl.grid(row=0, column=0, padx=2, pady=2)

rollno_ent = tk.Entry(detail_frame, bd=7, font=("arial", 17), textvariable=rollno)
rollno_ent.grid(row=0, column=1, padx=2, pady=2)

name_lbl = tk.Label(detail_frame, text="Name ", font=('Arial', 15), bg="lightgrey")
name_lbl.grid(row=1, column=0, padx=2, pady=2)

name_ent = tk.Entry(detail_frame, bd=7, font=("arial", 17), textvariable=name)
name_ent.grid(row=1, column=1, padx=2, pady=2)

class_lbl = tk.Label(detail_frame, text="Class ", font=('Arial', 15), bg="lightgrey")
class_lbl.grid(row=2, column=0, padx=2, pady=2)

class_ent = tk.Entry(detail_frame, bd=7, font=("arial", 17), textvariable=class_)
class_ent.grid(row=2, column=1, padx=2, pady=2)

section_lbl = tk.Label(detail_frame, text="Section ", font=('Arial', 15), bg="lightgrey")
section_lbl.grid(row=3, column=0, padx=2, pady=2)

section_ent = tk.Entry(detail_frame, bd=7, font=("arial", 17), textvariable=section)
section_ent.grid(row=3, column=1, padx=2, pady=2)

contact_lbl = tk.Label(detail_frame, text="Contact ", font=('Arial', 15), bg="lightgrey")
contact_lbl.grid(row=4, column=0, padx=2, pady=2)

contact_ent = tk.Entry(detail_frame, bd=7, font=("arial", 17), textvariable=contact)
contact_ent.grid(row=4, column=1, padx=2, pady=2)

fathers_lbl = tk.Label(detail_frame, text="Father's Name ", font=('Arial', 15), bg="lightgrey")
fathers_lbl.grid(row=5, column=0, padx=2, pady=2)

fathers_ent = tk.Entry(detail_frame, bd=7, font=("arial", 17), textvariable=fathers_name)
fathers_ent.grid(row=5, column=1, padx=2, pady=2)

address_lbl = tk.Label(detail_frame, text="Address ", font=('Arial', 15), bg="lightgrey")
address_lbl.grid(row=6, column=0, padx=2, pady=2)

address_ent = tk.Entry(detail_frame, bd=7, font=("arial", 17), textvariable=address)
address_ent.grid(row=6, column=1, padx=2, pady=2)

gender_lbl = tk.Label(detail_frame, text="Gender ", font=('Arial', 15), bg="lightgrey")
gender_lbl.grid(row=7, column=0, padx=2, pady=2)

gender_ent = ttk.Combobox(detail_frame, font=('Arial', 15), width=14, state='readonly', textvariable=gender)
gender_ent['values'] = ("Male", "Female", "Others")
gender_ent.grid(row=7, column=1, padx=2, pady=2)

dob_lbl = tk.Label(detail_frame, text="Date of Birth", font=('Arial', 15), bg="lightgrey")
dob_lbl.grid(row=8, column=0, padx=2, pady=2)

dob_ent = tk.Entry(detail_frame, bd=7, font=("arial", 17), textvariable=dob)
dob_ent.grid(row=8, column=1, padx=2, pady=2)

#============== Functions =====================

def fetch_data():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        curr.execute("SELECT * FROM data")
        rows = curr.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('', tk.END, values=row)
        conn.close()
    except Exception as e:
        print(f"Error fetching data: {str(e)}")

def add_data():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        roll_no = rollno.get()
        name_ = name.get()
        class__ = class_.get()
        section_ = section.get()
        contact_ = contact.get()
        fathers_name_ = fathers_name.get()
        address_ = address.get()
        gender_ = gender.get()
        dob_ = dob.get()
        curr.execute("INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                     (roll_no, name_, class__, section_, contact_, fathers_name_, address_, gender_, dob_))
        conn.commit()
        conn.close()
        student_table.insert('', 'end', values=(roll_no, name_, class__, section_, contact_, fathers_name_, address_, gender_, dob_))
        clear_fields()
    except Exception as e:
        print(f"Error adding data: {str(e)}")

def clear_fields():
    rollno.set("")
    name.set("")
    class_.set("")
    section.set("")
    contact.set("")
    fathers_name.set("")
    address.set("")
    gender.set("")
    dob.set("")

def update_data():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        roll_no = rollno.get()
        name_ = name.get()
        class__ = class_.get()
        section_ = section.get()
        contact_ = contact.get()
        fathers_name_ = fathers_name.get()
        address_ = address.get()
        gender_ = gender.get()
        dob_ = dob.get()
        curr.execute("UPDATE data SET Name=%s, Class=%s, Section=%s, Contact=%s, FathersName=%s, Address=%s, Gender=%s, DOB=%s WHERE RollNo=%s",
                     (name_, class__, section_, contact_, fathers_name_, address_, gender_, dob_, roll_no))
        conn.commit()
        conn.close()
        selected_item = student_table.selection()[0]
        student_table.item(selected_item, values=(roll_no, name_, class__, section_, contact_, fathers_name_, address_, gender_, dob_))
    except Exception as e:
        print(f"Error updating data: {str(e)}")

def delete_data():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        roll_no = rollno.get()
        curr.execute("DELETE FROM data WHERE RollNo=%s", (roll_no,))
        conn.commit()
        conn.close()
        selected_item = student_table.selection()[0]
        student_table.delete(selected_item)
        clear_fields()
    except Exception as e:
        print(f"Error deleting data: {str(e)}")

#========== Buttons ==========#

btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=20, y=450, width=380, height=120)

add_btn = tk.Button(btn_frame, text="Add", command=add_data, bd=7, font=("Arial", 13), width=12)
add_btn.grid(row=0, column=0, padx=2, pady=2)

update_btn = tk.Button(btn_frame, text="Update", command=update_data, bd=7, font=("Arial", 13), width=12)
update_btn.grid(row=0, column=1, padx=2, pady=2)

delete_btn = tk.Button(btn_frame, text="Delete", command=delete_data, bd=7, font=("Arial", 13), width=12)
delete_btn.grid(row=0, column=2, padx=2, pady=2)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_fields, bd=7, font=("Arial", 13), width=12)
clear_btn.grid(row=1, column=1, padx=2, pady=2)

search_frame = tk.Frame(data_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(search_frame, text="Search", bg="lightgrey", font=("Arial", 14))
search_lbl.grid(row=0, column=0, padx=10, pady=10)

search_in = ttk.Combobox(search_frame, font=("Arial", 14), state="readonly")
search_in['values'] = ("Roll No", "Name", "Class", "Section", "Father's Name", "Address", "Gender", "Date of Birth")
search_in.grid(row=0, column=1, padx=10, pady=10)

search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), bd=7, width=12, bg="lightgrey")
search_btn.grid(row=0, column=2, padx=10, pady=10)

showall_btn = tk.Button(search_frame, text="Show All", font=("Arial", 13), bd=7, width=12, bg="lightgrey", command=fetch_data)
showall_btn.grid(row=0, column=3, padx=10, pady=10)

#======== Database frame=======

main_frame = tk.Frame(data_frame, bg="lightgrey", bd=11, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

student_table = ttk.Treeview(main_frame, columns=("Roll No", "Name", "Class", "Section", "Contact", "Father's Name", "Address", "Gender", "Date of Birth"),
                             yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading("Roll No", text="Roll No")
student_table.heading("Name", text="Name")
student_table.heading("Class", text="Class")
student_table.heading("Section", text="Section")
student_table.heading("Contact", text="Contact")
student_table.heading("Father's Name", text="Father's Name")
student_table.heading("Address", text="Address")
student_table.heading("Gender", text="Gender")
student_table.heading("Date of Birth", text="Date of Birth")

student_table['show'] = 'headings'

student_table.column("Roll No", width=100)
student_table.column("Name", width=100)
student_table.column("Class", width=100)
student_table.column("Section", width=100)
student_table.column("Contact", width=100)
student_table.column("Father's Name", width=150)
student_table.column("Address", width=150)
student_table.column("Gender", width=100)
student_table.column("Date of Birth", width=100)

student_table.pack(fill=tk.BOTH, expand=True)

# Fetching initial data on startup
fetch_data()

win.mainloop()
