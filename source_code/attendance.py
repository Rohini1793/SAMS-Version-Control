# Student Attendance Management System

students = ["Amit", "Neha", "Rahul", "Priya"]

print("STUDENT ATTENDANCE MANAGEMENT SYSTEM")
print("------------------------------------")

for student in students:
    status = input(f"Enter attendance for {student} (P/A): ")
    print(student, "-", "Present" if status.upper() == "P" else "Absent")
