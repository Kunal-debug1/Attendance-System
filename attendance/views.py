from django.shortcuts import render, redirect, get_object_or_404
from .models import Student,Attendance


#Student list
 
def student_list(request):
  students = Student.objects.all()
  return render(request, "students.html",{'students' : students})

#Add student

def add_student(request):
  if request.method == "POST":
    name = request.POST['name']
    roll_no = request.POST['roll_no']
    Student.objects.create(name=name, roll_no=roll_no)
    return redirect('student_list')
  return render(request, 'add_student.html')

# Mark Attendence

def mark_attendance(request):
    students = Student.objects.all()

    if request.method == "POST":
        selected_date = request.POST.get("date")

        for student in students:
            # checkbox name = student.id
            is_present = str(student.id) in request.POST

            Attendance.objects.update_or_create(
                student=student,
                date=selected_date,
                defaults={'status': is_present}
            )

        return redirect('attendance_list')

    return render(request, "mark_attendance.html", {'students': students})


#Attendance List

def attendance_list(request):
    records = Attendance.objects.select_related('student').all()
    return render(request, 'attendance_list.html', {'records': records})


# DELETE ATTENDANCE
def delete_attendance(request, id):
    record = get_object_or_404(Attendance, id=id)
    record.delete()
    return redirect('attendance_list')

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.roll_no = request.POST['roll_no']
        student.save()
        return redirect('student_list')

    return render(request, 'edit_student.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect('student_list')

    return render(request, 'delete_student.html', {'student': student})
