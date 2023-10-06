from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
import datetime
from .models import CustomUser, Teacher,   Students, Attendance, AttendanceReport, StudentResult

#student home
def main(request):
    if request.method=='POST':
        return render(request, 'student templates/main.html')
    else:
        return render(request, 'student templates/main.html')
    
def student_home(request):
    student_obj = Students.objects.get(admin=request.user.id)
    total_attendance =   AttendanceReport.objects.filter(student_id=student_obj).count()
    attendance_present = AttendanceReport.objects.filter(student_id=student_obj,
                                                       status=True).count()
    attendance_absent =  AttendanceReport.objects.filter(student_id=student_obj,
                                                       status=False).count()
    data_present = []
    data_absent = []
    context={
        "total_attendance": total_attendance,
        "attendance_present": attendance_present,
        "attendance_absent": attendance_absent,
        "data_present": data_present,
        "data_absent": data_absent
    }

def student_view_attendance(request):
    student = Students.objects.get(admin=request.user.id)
    context={}
    return render(request, "student templates/student_view_attendance.html", context)

def student_view_attendance_post(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('student_view_attendance')
    else:
        # Getting all the Input Data
        
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
 
        # Parsing the date data into Python object
        start_date_parse = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date_parse = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
 
        # Getting all the Subject Data based on Selected Subject
        
         
        # Getting Logged In User Data
        user_obj = CustomUser.objects.get(id=request.user.id)
         
        # Getting Student Data Based on Logged in Data
        stud_obj = Students.objects.get(admin=user_obj)
 
        # Now Accessing Attendance Data based on the Range of Date
        # Selected and Subject Selected
        attendance = Attendance.objects.filter(attendance_date__range=(start_date_parse,
                                                                       end_date_parse),
                                               )
        # Getting Attendance Report based on the attendance
        # details obtained above
        attendance_reports = AttendanceReport.objects.filter(attendance_id__in=attendance,
                                                             student_id=stud_obj)
 
         
        context = {
            "attendance_reports": attendance_reports
        }
 
        '''return render(request, 'student_template/student_attendance_data.html', context)'''
        return render(request, 'student templates/student_view_attendance.html', context)

    
def student_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)
 
    context={
        "user": user,
        "student": student
    }
    return render(request, 'student templates/student_profile.html', context)
 
 
def student_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('student_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
 
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
 
            student = Students.objects.get(admin=customuser.id)
            student.save()
             
            messages.success(request, "Profile Updated Successfully")
            return redirect('student_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('student_profile')
 
 
def student_view_result(request):
    student = Students.objects.get(admin=request.user.id)
    student_result = StudentResult.objects.filter(student_id=student.id)
    context = {
        "student_result": student_result,
    }
    return render(request, "student templates/student_view_result.html", context)
        
