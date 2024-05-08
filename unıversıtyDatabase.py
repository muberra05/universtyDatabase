import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from mysql.connector import connect, Error

class UniversityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("University Management System")

        # Database connection
        self.conn = connect(
            host="localhost",
            user="root",
            password="7607",
            database="university",
        )
        self.cursor = self.conn.cursor()

        # Create tables if they don't exist
        self.create_tables()

        # Create UI components
        self.create_widgets()

    def create_tables(self):
       # Create Students table
        create_students_table_query = """
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT,
                INDEX (name)
            ) DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci
        """
        self.run_query(create_students_table_query)

        # Create Courses table
        create_courses_table_query = """
            CREATE TABLE IF NOT EXISTS courses (
                id INT AUTO_INCREMENT PRIMARY KEY,
                course_name VARCHAR(255) NOT NULL,
                credit_hours INT,
                INDEX (course_name)
            ) DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci
        """
        self.run_query(create_courses_table_query)

        # Create Instructors table
        create_instructors_table_query = """
            CREATE TABLE IF NOT EXISTS instructors (
                id INT AUTO_INCREMENT PRIMARY KEY,
                instructor_name VARCHAR(255) NOT NULL,
                department VARCHAR(255)
            ) DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci
        """
        self.run_query(create_instructors_table_query)

        # Create Enrollments table
        create_enrollments_table_query = """
            CREATE TABLE IF NOT EXISTS enrollments (
                id INT AUTO_INCREMENT PRIMARY KEY,
                student_id INT NOT NULL,
                course_id INT NOT NULL,
                INDEX (student_id),
                INDEX (course_id)
            ) DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci
        """
        self.run_query(create_enrollments_table_query)
# Kullanıcı adı ve şifre kontrolü için giriş ekranı
        self.create_login_screen()

    def create_login_screen(self):
        # Kullanıcı adı ve şifre kontrolü için giriş ekranı oluştur
     login_frame = Frame(self.root, bg="#f0f0f0")
     login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Kullanıcı adı ve şifre etiketleri
     username_label = Label(login_frame, text="Username:", bg="#f0f0f0")
     username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

     password_label = Label(login_frame, text="Password:", bg="#f0f0f0")
     password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        # Kullanıcı adı ve şifre giriş alanları
     username_entry = Entry(login_frame)
     username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

     password_entry = Entry(login_frame, show="*")
     password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Giriş butonu
     login_button = Button(login_frame, text="Login", command=lambda: self.check_login(username_entry.get(), password_entry.get()))
     login_button.grid(row=2, columnspan=2, pady=10)

    def check_login(self, username, password):
        # Kullanıcı adı ve şifre kontrolü
        if username == "admin" and password == "password123":
            # Doğruysa ana sayfa butonları oluştur
            self.create_main_buttons()
        else:
            # Yanlışsa uyarı ver
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    
    def create_widgets(self):
        # Tabs
        self.tabs = ttk.Notebook(self.root)
        self.student_tab = ttk.Frame(self.tabs)
        self.course_tab = ttk.Frame(self.tabs)
        self.enrollment_tab = ttk.Frame(self.tabs)
        self.instructor_tab = ttk.Frame(self.tabs)

        self.tabs.add(self.student_tab, text="Students")
        self.tabs.add(self.course_tab, text="Courses")
        self.tabs.add(self.enrollment_tab, text="Enrollments")
        self.tabs.add(self.instructor_tab, text="Instructors")

        self.tabs.pack(expand=1, fill="both")

        # Student Tab
        self.create_student_tab()

        # Course Tab
        self.create_course_tab()

        # Enrollment Tab
        self.create_enrollment_tab()

        # Instructor Tab
        self.create_instructor_tab()

    def create_student_tab(self):
        # Widgets for Students tab
        label_name = tk.Label(self.student_tab, text="Name:")
        entry_name = tk.Entry(self.student_tab)
        label_age = tk.Label(self.student_tab, text="Age:")
        entry_age = tk.Entry(self.student_tab)
        btn_insert = tk.Button(self.student_tab, text="Insert", command=lambda: self.insert_student(entry_name.get(), entry_age.get()))
        btn_delete = tk.Button(self.student_tab, text="Delete", command=lambda: self.delete_student(entry_name.get()))
        btn_update = tk.Button(self.student_tab, text="Update", command=lambda: self.update_student(entry_name.get(), entry_age.get()))
        btn_list = tk.Button(self.student_tab, text="List", command=self.list_students)

        # Grid layout
        label_name.grid(row=0, column=0, padx=5, pady=5)
        entry_name.grid(row=0, column=1, padx=5, pady=5)
        label_age.grid(row=1, column=0, padx=5, pady=5)
        entry_age.grid(row=1, column=1, padx=5, pady=5)
        btn_insert.grid(row=2, column=0, padx=5, pady=5)
        btn_delete.grid(row=2, column=1, padx=5, pady=5)
        btn_update.grid(row=2, column=2, padx=5, pady=5)
        btn_list.grid(row=2, column=3, padx=5, pady=5)

    def create_course_tab(self):
        # Widgets for Courses tab
        label_course_name = tk.Label(self.course_tab, text="Course Name:")
        entry_course_name = tk.Entry(self.course_tab)
        label_credit_hours = tk.Label(self.course_tab, text="Credit Hours:")
        entry_credit_hours = tk.Entry(self.course_tab)
        btn_insert = tk.Button(self.course_tab, text="Insert", command=lambda: self.insert_course(entry_course_name.get(), entry_credit_hours.get()))
        btn_delete = tk.Button(self.course_tab, text="Delete", command=lambda: self.delete_course(entry_course_name.get()))
        btn_update = tk.Button(self.course_tab, text="Update", command=lambda: self.update_course(entry_course_name.get(), entry_credit_hours.get()))
        btn_list = tk.Button(self.course_tab, text="List", command=self.list_courses)

        # Grid layout
        label_course_name.grid(row=0, column=0, padx=5, pady=5)
        entry_course_name.grid(row=0, column=1, padx=5, pady=5)
        label_credit_hours.grid(row=1, column=0, padx=5, pady=5)
        entry_credit_hours.grid(row=1, column=1, padx=5, pady=5)
        btn_insert.grid(row=2, column=0, padx=5, pady=5)
        btn_delete.grid(row=2, column=1, padx=5, pady=5)
        btn_update.grid(row=2, column=2, padx=5, pady=5)
        btn_list.grid(row=2, column=3, padx=5, pady=5)

    def create_enrollment_tab(self):
        
        # Widgets for Enrollments tab
        label_student_name = tk.Label(self.enrollment_tab, text="Student ID:")
        entry_student_name = tk.Entry(self.enrollment_tab)
        label_course_name = tk.Label(self.enrollment_tab, text="Course ID:")
        entry_course_name = tk.Entry(self.enrollment_tab)
        btn_insert = tk.Button(self.enrollment_tab, text="Insert", command=lambda: self.insert_enrollment(entry_student_name.get(), entry_course_name.get()))
        btn_delete = tk.Button(self.enrollment_tab, text="Delete", command=lambda: self.delete_enrollment(entry_student_name.get(), entry_course_name.get()))
        btn_list = tk.Button(self.enrollment_tab, text="List", command=self.list_enrollments)

        # Grid layout
        label_student_name.grid(row=0, column=0, padx=5, pady=5)
        entry_student_name.grid(row=0, column=1, padx=5, pady=5)
        label_course_name.grid(row=1, column=0, padx=5, pady=5)
        entry_course_name.grid(row=1, column=1, padx=5, pady=5)
        btn_insert.grid(row=2, column=0, padx=5, pady=5)
        btn_delete.grid(row=2, column=1, padx=5, pady=5)
        btn_list.grid(row=2, column=2, padx=5, pady=5)

    def create_instructor_tab(self):
        # Widgets for Instructors tab
        label_instructor_name = tk.Label(self.instructor_tab, text="Instructor Name:")
        entry_instructor_name = tk.Entry(self.instructor_tab)
        label_department = tk.Label(self.instructor_tab, text="Department:")
        entry_department = tk.Entry(self.instructor_tab)
        btn_insert = tk.Button(self.instructor_tab, text="Insert", command=lambda: self.insert_instructor(entry_instructor_name.get(), entry_department.get()))
        btn_delete = tk.Button(self.instructor_tab, text="Delete", command=lambda: self.delete_instructor(entry_instructor_name.get()))
        btn_update = tk.Button(self.instructor_tab, text="Update", command=lambda: self.update_instructor(entry_instructor_name.get(), entry_department.get()))
        btn_list = tk.Button(self.instructor_tab, text="List", command=self.list_instructors)

        # Grid layout
        label_instructor_name.grid(row=0, column=0, padx=5, pady=5)
        entry_instructor_name.grid(row=0, column=1, padx=5, pady=5)
        label_department.grid(row=1, column=0, padx=5, pady=5)
        entry_department.grid(row=1, column=1, padx=5, pady=5)
        btn_insert.grid(row=2, column=0, padx=5, pady=5)
        btn_delete.grid(row=2, column=1, padx=5, pady=5)
        btn_update.grid(row=2, column=2, padx=5, pady=5)
        btn_list.grid(row=2, column=3, padx=5, pady=5)

    def run_query(self, query, data=None):
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return True
        except Error as e:
            messagebox.showerror("Error", f"Database Error: {e}")
            return False

    def insert_student(self, name, age):
        query = "INSERT INTO students (name, age) VALUES (%s, %s)"
        data = (name, age)
        if self.run_query(query, data):
            messagebox.showinfo("Success", "Student inserted successfully.")
        else:
            messagebox.showerror("Error", "Failed to insert student.")

    def delete_student(self, name):
        query = "DELETE FROM students WHERE name = %s"
        if self.run_query(query, (name,)):
            messagebox.showinfo("Success", "Student deleted successfully.")
        else:
            messagebox.showerror("Error", "Failed to delete student.")

    def update_student(self, name, age):
        query = "UPDATE students SET age = %s WHERE name = %s"
        data = (age, name)
        if self.run_query(query, data):
            messagebox.showinfo("Success", "Student updated successfully.")
        else:
            messagebox.showerror("Error", "Failed to update student.")

    def list_students(self):
        query = "SELECT * FROM students"
        students = self.fetch_data(query)
        if students:
            messagebox.showinfo("Students", "\n".join([f"ID: {s[0]}, Name: {s[1]}, Age: {s[2]}" for s in students]))
        else:
            messagebox.showinfo("Students", "No students found.")

    def insert_course(self, course_name, credit_hours):
        query = "INSERT INTO courses (course_name, credit_hours) VALUES (%s, %s)"
        data = (course_name, credit_hours)
        if self.run_query(query, data):
            messagebox.showinfo("Success", "Course inserted successfully.")
        else:
            messagebox.showerror("Error", "Failed to insert course.")

    def delete_course(self, course_name):
        query = "DELETE FROM courses WHERE course_name = %s"
        if self.run_query(query, (course_name,)):
            messagebox.showinfo("Success", "Course deleted successfully.")
        else:
            messagebox.showerror("Error", "Failed to delete course.")

    def update_course(self, course_name, credit_hours):
        query = "UPDATE courses SET credit_hours = %s WHERE course_name = %s"
        data = (credit_hours, course_name)
        if self.run_query(query, data):
            messagebox.showinfo("Success", "Course updated successfully.")
        else:
            messagebox.showerror("Error", "Failed to update course.")

    def list_courses(self):
        query = "SELECT * FROM courses"
        courses = self.fetch_data(query)
        if courses:
            messagebox.showinfo("Courses", "\n".join([f"ID: {c[0]}, Course Name: {c[1]}, Credit Hours: {c[2]}" for c in courses]))
        else:
            messagebox.showinfo("Courses", "No courses found.")

    def insert_enrollment(self, student_id, course_id):
        query = "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)"
        data = (student_id, course_id)
        if self.run_query(query, data):
            messagebox.showinfo("Success", "Enrollment added successfully.")
        else:
            messagebox.showerror("Error", "Failed to add enrollment.")

    def delete_enrollment(self, student_id, course_id):
        query = "DELETE FROM enrollments WHERE student_id = %s AND course_id = %s"
        if self.run_query(query, (student_id, course_id)):
            messagebox.showinfo("Success", "Enrollment deleted successfully.")
        else:
            messagebox.showerror("Error", "Failed to delete enrollment.")

    def list_enrollments(self):
        query = "SELECT * FROM enrollments"
        enrollments = self.fetch_data(query)
        if enrollments:
            messagebox.showinfo("Enrollments", "\n".join([f"ID: {e[0]}, Student Id: {e[1]}, Course Id: {e[2]}" for e in enrollments]))
        else:
            messagebox.showinfo("Enrollments", "No enrollments found.")

    def insert_instructor(self, instructor_name, department):
        query = "INSERT INTO instructors (instructor_name, department) VALUES (%s, %s)"
        data = (instructor_name, department)
        if self.run_query(query, data):
            messagebox.showinfo("Success", "Instructor added successfully.")
        else:
            messagebox.showerror("Error", "Failed to add instructor.")

    def delete_instructor(self, instructor_name):
        query = "DELETE FROM instructors WHERE instructor_name = %s"
        if self.run_query(query, (instructor_name,)):
            messagebox.showinfo("Success", "Instructor deleted successfully.")
        else:
            messagebox.showerror("Error", "Failed to delete instructor.")

    def update_instructor(self, instructor_name, department):
        query = "UPDATE instructors SET department = %s WHERE instructor_name = %s"
        data = (department, instructor_name)
        if self.run_query(query, data):
            messagebox.showinfo("Success", "Instructor updated successfully.")
        else:
            messagebox.showerror("Error", "Failed to update instructor.")

    def list_instructors(self):
        query = "SELECT * FROM instructors"
        instructors = self.fetch_data(query)
        if instructors:
            messagebox.showinfo("Instructors", "\n".join([f"ID: {i[0]}, Instructor Name: {i[1]}, Department: {i[2]}" for i in instructors]))
        else:
            messagebox.showinfo("Instructors", "No instructors found.")

    def fetch_data(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            messagebox.showerror("Error", f"Database Error: {e}")
            return []

if __name__== "__main__":
    root = tk.Tk()
    app = UniversityApp(root)
    root.mainloop()