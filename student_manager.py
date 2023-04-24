import tkinter as tk
from tkinter import ttk, messagebox

class Student:
    def __init__(self, name, age, gender, class_):
        self.name = name
        self.age = age
        self.gender = gender
        self.class_ = class_

def read_students():
    students = []
    with open('students.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            name, age, gender, class_ = line.strip().split(',')
            students.append(Student(name, age, gender, class_))
    return students

def write_students(students):
    with open('students.txt', 'w') as file:
        for student in students:
            file.write(f'{student.name},{student.age},{student.gender},{student.class_}\n')

def refresh_treeview():
    treeview.delete(*treeview.get_children())
    for student in students:
        treeview.insert('', tk.END, values=(student.name, f'{student.age} years old', student.gender, f'class {student.class_}'))

def add_student():
    try:
        new_student = Student(entry_name.get(), entry_age.get(), entry_gender.get(), entry_class.get())
        students.append(new_student)
        write_students(students)
        refresh_treeview()
        messagebox.showinfo("Success", "Student information added successfully!")
    except Exception as e:
        messagebox.showerror("Error", "Add failed, please check if the input is correct.")

def edit_student():
    try:
        selected_item = treeview.selection()[0]
        selected = treeview.item(selected_item)
        index = treeview.get_children().index(selected_item)
        students[index].name = entry_name.get()
        students[index].age = entry_age.get()
        students[index].gender = entry_gender.get()
        students[index].class_ = entry_class.get()
        write_students(students)
        refresh_treeview()
        messagebox.showinfo("Success", "Student information modified successfully!")
    except Exception as e:
        messagebox.showerror("Error", "Modification failed, please check if the input is correct.")

def search_student():
    name = entry_name.get()
    found_students = [student for student in students if student.name == name]
    if found_students:
        treeview.delete(*treeview.get_children())
        for student in found_students:
            treeview.insert('', tk.END, values=(student.name, f'{student.age} years old', student.gender, f'class {student.class_}'))
    else:
        messagebox.showerror("Error", "Student not found, please check if the input is correct.")

def delete_student():
    try:
        selected_item = treeview.selection()[0]
        index = treeview.get_children().index(selected_item)
        students.pop(index)
        write_students(students)
        refresh_treeview()
        messagebox.showinfo("Success", "Student information deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", "Deletion failed, please select a student.")

students = read_students()

root = tk.Tk()
root.title("Student Information Management System")
root.configure(bg='lightblue')

frame_top = tk.Frame(root, bg='lightblue')
frame_top.pack(side=tk.TOP, padx=10, pady=10)

frame_bottom = tk.Frame(root, bg='lightblue')
frame_bottom.pack(side=tk.BOTTOM, padx=10, pady=10)

style = ttk.Style()
style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
style.configure("Treeview", anchor=tk.W)
style.configure("Treeview.Cell", anchor=tk.CENTER)

treeview = ttk.Treeview(frame_top, columns=("Name", "Age", "Gender", "Class"), show="headings")
treeview.heading("Name", text="Name", anchor=tk.W)
treeview.heading("Age", text="Age", anchor=tk.W)
treeview.heading("Gender", text="Gender", anchor=tk.W)
treeview.heading("Class", text="Class", anchor=tk.W)
treeview.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

entry_name = tk.Entry(frame_bottom)
entry_name.grid(row=0, column=0)
label_name = tk.Label(frame_bottom, text="Name", bg='lightblue')
label_name.grid(row=1, column=0)

entry_age = tk.Entry(frame_bottom)
entry_age.grid(row=0, column=1)
label_age = tk.Label(frame_bottom, text="Age", bg='lightblue')
label_age.grid(row=1, column=1)

entry_gender = tk.Entry(frame_bottom)
entry_gender.grid(row=0, column=2)
label_gender = tk.Label(frame_bottom, text="Gender", bg='lightblue')
label_gender.grid(row=1, column=2)

entry_class = tk.Entry(frame_bottom)
entry_class.grid(row=0, column=3)
label_class = tk.Label(frame_bottom, text="Class", bg='lightblue')
label_class.grid(row=1, column=3)

button_add = tk.Button(frame_bottom, text="Add", command=add_student, bg='#4CAF50', activebackground='#2E7D32', bd=0)
button_add.grid(row=2, column=0, pady=10)

button_edit = tk.Button(frame_bottom, text="Edit", command=edit_student, bg='#2196F3', activebackground='#1565C0', bd=0)
button_edit.grid(row=2, column=1, pady=10)

button_search = tk.Button(frame_bottom, text="Search", command=search_student, bg='#FF9800', activebackground='#EF6C00', bd=0)
button_search.grid(row=2, column=2, pady=10)

button_delete = tk.Button(frame_bottom, text="Delete", command=delete_student, bg='#F44336', activebackground='#C62828', bd=0)
button_delete.grid(row=2, column=3, pady=10)

refresh_treeview()

root.mainloop()

