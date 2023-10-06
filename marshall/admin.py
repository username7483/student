from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Teacher,Students,Attendance,AttendanceReport,NotificationStudent,NotificationStaffs

# Register your models here.
class UserModel(UserAdmin):
    pass
admin.site.register(CustomUser,UserModel)
admin.site.register(Teacher)
admin.site.register(Students)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)

# Register your models here.
