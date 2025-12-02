# Attendance Management System

A basic Django web application to manage students and track attendance.

## Features
- Add / Edit / Delete students
- Mark attendance (Present / Absent)
- View attendance records
- Prevent duplicate attendance per student per date
- Simple and clean UI

## Tech Stack
- Python
- Django
- SQLite
- HTML, CSS, Bootstrap

## Screenshots : 

- Students: 

<img width="1920" height="1020" alt="Screenshot 2025-12-02 152754" src="https://github.com/user-attachments/assets/88ba6f14-6964-42c9-b868-60ef9f38051f" />

- Add Student:

<img width="1920" height="1020" alt="Screenshot 2025-12-02 152836" src="https://github.com/user-attachments/assets/6c20c7a7-b664-4e3b-b2f3-ee4501676d6c" />

- Delete Student:

<img width="1920" height="1020" alt="Screenshot 2025-12-02 153204" src="https://github.com/user-attachments/assets/771ca469-2461-415e-a0c1-cf5ed6eaf9fd" />

- Mark Attendence:

<img width="1920" height="1020" alt="Screenshot 2025-12-02 152854" src="https://github.com/user-attachments/assets/239871db-cc91-457e-ad26-aad56736c357" />

- Attendance List:

<img width="1920" height="1020" alt="Screenshot 2025-12-02 152908" src="https://github.com/user-attachments/assets/bd4f68a8-4d1c-4f9e-b854-4f7605d46f72" />

## Setup
```bash
git clone <repo-url>
cd project
python manage.py migrate
python manage.py runserver
