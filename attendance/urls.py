from django.urls import path

from .import views

urlpatterns = [
  path('', views.student_list, name='student_list'),
  path('add/', views.add_student, name="add_student"),
  path('mark/', views.mark_attendance, name="mark_attendance"),
  path('attendance/',views.attendance_list, name="attendance_list"),
  path('delete/<int:id>/', views.delete_attendance, name="delete_attendance"),
  path('edit/<int:id>/', views.edit_student, name='edit_student'),
  path('student/delete/<int:id>/', views.delete_student, name='delete_student'),


]