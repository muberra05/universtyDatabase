mport tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from mysql.connector import connect, Error

class UniversityApp:
    def init(self, root):
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