from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #import django user sign up form
from django.contrib.auth.models import User #import user model
from django.db import IntegrityError #import for error catching 
from django.contrib.auth import login,logout,authenticate #allow actual action of logging in / out

# Create your views here.

def signupuser(request):
    #if method GET display signup user form - if post 
    if request.method == 'GET':
        return render(request, 'notes/signupuser.html', {'form':UserCreationForm()}) # importing UserCreation form is used here (UserCreationForm())

    else:
        #create new user 
        if request.POST['password1'] == request.POST['password2']: #check if passwords match
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) #pass user.objects.create_user items in request.POST(dictionary)
                user.save() # actually save user to database
                login(request, user) #login user then we need to send them somewhere
                return redirect('reminder') #send user to reminder
            except IntegrityError: #got error type from error page on site (caused by duplicate username attempt at account creation)
       
                return render(request, 'notes/signupuser.html', {'form':UserCreationForm(), 'error':'That Username has already been taken. Please choose a new username.'}) #passwords did not match send back form and state no match
    
        else:
             #tell users passwords didnt match
            return render(request, 'notes/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'}) #passwords did not match send back form and state no match
       
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'notes/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'], password=request.POST['password']) #set user to authentication request django method
        if user is None: #if auth failed
            return render(request, 'notes/loginuser.html', {'form':AuthenticationForm(), 'error':"username or password incorrect"})
        else:
            login(request, user) #if auth successful, log user in
            return redirect('reminder') #send user to reminder




def logoutuser(request):
    if request.method == 'POST': #Method is post because browsers can automatically send GET req for links (like logout)
        logout(request)
        return redirect('home')


def reminder(request): #actual app 'reminder' 
    return render(request, 'notes/reminder.html')

def home(request): #home page
    return render(request, 'notes/home.html')


