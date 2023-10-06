from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from marshall import models
from .models import CustomUser, Teacher, Students

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.
'''def choice(request):
    if request.method=='POST':
        if "enter" in request.POST:
            return redirect('login')
    else:
        return render(request,'choice.html')
    
def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User = get_user_model()
        try:
            user = User.objects.get(username=username)
            #user = User.objects.create_user(username=username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            # Password is correct, log the user in and redirect to the home page
            login(request, user)
            return redirect('home')
        else:
            # Display an error message if the username or password is incorrect
            error_message = "Invalid username or password."
            return render(request, 'signin.html', {'error_message': error_message})
    else:
        return render(request, 'signin.html')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        pass2 = request.POST['pass2']

        if password == pass2:
            
            # Create and save the user to the database
            
            User = get_user_model()
            user = User.objects.create_user(username=username, password=password)
            #user = USER(username=username, fname=fname, lname=lname, email=email, password=password)
            user.save()

            # Redirect to login page with a success msg
            success_message = "Account created successfully. You can now log in."
            return render(request, 'signin.html', {'success_message': success_message})
        else:
            # Display an error message if passwords don't match
            error_message = "Passwords do not match."
            return render(request, 'register.html', {'error_message': error_message})
        
    return render(request, 'register.html')

def home(request):
    if request.method=='POST':
        return render(request,'home.html')
    else:
        return render(request,'home.html')
    '''
def home(request):
    return render(request,'home.html')

def settings(request):
    return render(request,'settings.html')

def loginUser(request):
    if request.method=='POST':
        return render(request, 'login_page.html')
    else:
        return render(request, 'login_page.html')
    
def doLogin(request):

        if request.method=='POST':
            email_id = request.POST['email']
            password = request.POST['password']

        if not (email_id and password):
            messages.error(request, "Please provide all the details!!")
            return render(request, 'login_page.html')

        user = authenticate(request, username=email_id, password=password)

        if not user:
            messages.error(request, 'Invalid Login Credentials!!')
            return render(request, 'login_page.html')
            # Password is correct, log the user in and redirect to the home page
        login(request, user)
        print(request.user)
        if user.user_type == CustomUser.STUDENT:
            return redirect('main')
        if user.user_type == CustomUser.TEACHER:
            return redirect('main2')
        return render(request,'home.html')
       

    
    
'''if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        User = get_user_model()
        
        try:
            user = User.objects.get(email=email)
            
        except User.DoesNotExist:
            user = None

        if not (email and password):
            messages.error(request, "Please provide all the details!!")
            return render(request, 'login_page.html')
    
        if user is not None and user.check_password(password):
        # Password is correct, log the user in and redirect to the home page
            login(request, user)
            if user.user_type == CustomUser.STUDENT:
                return redirect('main')
            elif user.user_type == CustomUser.TEACHER:
                return redirect('main2')
            else:
                return redirect('home')
            
        else:
            messages.error(request, 'Invalid Login Credentials!!')
            return render(request, 'login_page.html')

    else:
        return render(request, 'login_page.html')'''


 

def registration(request):
    return render(request,'registration.html')
     
 
def doRegistration(request):
    
    if request.method=='POST':
        #username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_id = request.POST['email']
        password = request.POST['password']
        pass2 = request.POST['confirmPassword']

        if not (email_id and password and pass2):
            messages.error(request, 'Please provide all the details!!')
            return render(request, 'registration.html')
        
        if password != pass2:
            messages.error(request, 'Both passwords should match!!')
            return render(request, 'registration.html')
        
        is_user_exists = CustomUser.objects.filter(email=email_id).exists()
        if is_user_exists:
            messages.error(request, 'User with this email id already exists. Please proceed to login!!')
            return render(request, 'registration.html')
        
        user_type = get_user_type_from_email(email_id)
 
        if user_type is None:
            messages.error(request, "Please use valid format for the email id: '<username>.<staff|student|hod>@<college_domain>'")
            return render(request, 'registration.html')
        
        username = email_id.split('@')[0].split('.')[0]
 
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'User with this username already exists. Please use different username')
            return render(request, 'registration.html')
        
          
        user = CustomUser()
        user.username = username
        user.email = email_id
        user.password = password
        user.user_type = user_type
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        '''user = user.objects.create_user(username=email_id, password=password)'''
            #user = USER(username=username, fname=fname, lname=lname, email=email, password=password)
        user.save()

        '''if user_type == CustomUser.TEACHER:
            Teacher.objects.create(admin=user)
                
        elif user_type == CustomUser.STUDENT:
            Students.objects.create(admin=user)
                

            messages.success(request, 'Account created successfully. You can now log in.')
            return render(request, 'login_page.html')
            success_message = "Account created successfully. You can now log in."
            return render(request, 'login_page.html', {'success_message': success_message})
            
        
    return render(request, 'registration.html')'''
 

def logout_view(request):
    return render(request, 'logout_user.html')


def get_user_type_from_email(email_id):
    """
    Returns CustomUser.user_type corresponding to the given email address
    email_id should be in following format:
    '<username>.<staff|student|hod>@<college_domain>'
    eg.: 'abhishek.staff@jecrc.com'
    """
 
    try:
        email_id = email_id.split('@')[0]
        email_user_type = email_id.split('.')[1]
        return CustomUser.EMAIL_TO_USER_TYPE_MAP[email_user_type]
    except:
        return None