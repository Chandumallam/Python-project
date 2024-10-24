import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize student data
students = {}

# Function to add student data
def add_student():
    name = name_entry.get()
    grade = grade_entry.get()
    attendance = attendance_entry.get()

    if not name or not grade or not attendance:
        messagebox.showerror("Error", "All fields must be filled.")
        return

    try:
        grade = float(grade)
        attendance = float(attendance)
    except ValueError:
        messagebox.showerror("Error", "Grade and attendance must be numbers.")
        return

    students[name] = {"grade": grade, "attendance": attendance}
    name_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    attendance_entry.delete(0, tk.END)

    update_charts()

# Function to update the performance charts
def update_charts():
    if not students:
        return

    names = list(students.keys())
    grades = [students[name]["grade"] for name in names]
    attendance = [students[name]["attendance"] for name in names]

    # Clear the axes
    ax1.clear()
    ax2.clear()

    # Plotting Grades
    ax1.bar(names, grades, color='#34495e')  # Dark blue bars
    ax1.set_title('Student Grades', fontsize=14, fontweight='bold', color='#34495e')
    ax1.set_xlabel('Students', fontsize=12, color='#34495e')
    ax1.set_ylabel('Grades', fontsize=12, color='#34495e')
    # Removed grid lines
    ax1.grid(False)

    # Plotting Attendance
    ax2.bar(names, attendance, color='#1abc9c')  # Green bars
    ax2.set_title('Student Attendance', fontsize=14, fontweight='bold', color='#34495e')
    ax2.set_xlabel('Students', fontsize=12, color='#34495e')
    ax2.set_ylabel('Attendance (%)', fontsize=12, color='#34495e')
    # Removed grid lines
    ax2.grid(False)

    # Adjust space between the graphs
    plt.subplots_adjust(hspace=0.5)

    # Redraw the canvas
    canvas.draw()

# GUI Setup
root = tk.Tk()
root.title("Student Performance Dashboard")

# Set window size and background color
root.geometry("900x700")
root.configure(bg="#ECF0F1")  # Light grey background

# Create main frame with padding
main_frame = tk.Frame(root, bg="#ffffff", bd=10, relief="flat")
main_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.9, anchor='n')

# Title label with custom font
title_label = tk.Label(main_frame, text="Student Performance Dashboard", font=("Helvetica", 24, 'bold'), fg="#34495e", bg="#ffffff")
title_label.pack(pady=20)

# Input frame for entry widgets
input_frame = tk.Frame(main_frame, bg="#ffffff")
input_frame.pack(pady=10, padx=20, fill='x')

# Input fields with modern design
tk.Label(input_frame, text="Student Name:", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky='w')
name_entry = ttk.Entry(input_frame, font=("Arial", 10), width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(input_frame, text="Grade:", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
grade_entry = ttk.Entry(input_frame, font=("Arial", 10), width=30)
grade_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(input_frame, text="Attendance (%):", bg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky='w')
attendance_entry = ttk.Entry(input_frame, font=("Arial", 10), width=30)
attendance_entry.grid(row=2, column=1, padx=10, pady=10)

# Styled button with hover effect
def on_enter(e):
    add_button['background'] = '#1abc9c'

def on_leave(e):
    add_button['background'] = '#16a085'

add_button = tk.Button(input_frame, text="Add Student", command=add_student, font=("Arial", 12, "bold"), bg="#16a085", fg="white", bd=0, padx=10, pady=5)
add_button.grid(row=3, columnspan=2, pady=20)
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)

# Chart frame for graphs
chart_frame = tk.Frame(main_frame, bg="#ffffff", relief="flat")
chart_frame.pack(padx=10, pady=10, fill='both', expand=True)

# Matplotlib setup for performance charts
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8), facecolor="#ffffff")
# Adjusting the space between the graphs
fig.subplots_adjust(hspace=0.5)  # Increased vertical space between plots

canvas = FigureCanvasTkAgg(fig, master=chart_frame)
canvas.get_tk_widget().pack(fill='both', expand=True)

# Start the application
root.mainloop()
