"""
URL configuration for edu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from marshall import views 

from django.contrib import admin
from django.urls import path, include
from  marshall  import views
from marshall import STAFFVIEWS,STUDENTVIEWS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/', views.loginUser, name="login"),
    path('logout_user/', views.logout, name="logout_user"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('registration/',views.registration,name='registration'),
    path('doRegistration/',views.doRegistration,name='doRegistration'),
    
    
    # STUDENT URLS
    path('main/',STUDENTVIEWS.main,name='main'),
    path('main/student_view_attendance/', STUDENTVIEWS.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post/', STUDENTVIEWS.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_profile/', STUDENTVIEWS.student_profile, name="student_profile"),
    path('main/student_profile_update/', STUDENTVIEWS.student_profile_update, name="student_profile_update"),
    path('main/student_view_result/', STUDENTVIEWS.student_view_result, name="student_view_result"),
    
    
    
    # TEACHER URLS
    path('main2/',STAFFVIEWS.main2,name="main2"),
    path('staff_take_attendance/', STAFFVIEWS.staff_take_attendance, name="staff_take_attendance"),
    path('get_students/', STAFFVIEWS.get_students, name="get_students"),
    path('save_attendance_data/', STAFFVIEWS.save_attendance_data, name="save_attendance_data"),
    path('staff_update_attendance/', STAFFVIEWS.staff_update_attendance, name="staff_update_attendance"),
    path('get_attendance_dates/', STAFFVIEWS.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student/', STAFFVIEWS.get_attendance_student, name="get_attendance_student"),
    path('update_attendance_data/', STAFFVIEWS.update_attendance_data, name="update_attendance_data"),
    path('staff_profile/', STAFFVIEWS.staff_profile, name="staff_profile"),
    path('staff_profile_update/', STAFFVIEWS.staff_profile_update, name="staff_profile_update"),
    path('staff_add_result/', STAFFVIEWS.staff_add_result, name="staff_add_result"),
    path('staff_add_result_save/', STAFFVIEWS.staff_add_result_save, name="staff_add_result_save"),
    
]


'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marshall.urls')),
    path('choice/',views.choice, name='choice'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('marshall/', include('django.contrib.auth.urls')),
    path('marshall/', include('marshall.urls')),
]'''
