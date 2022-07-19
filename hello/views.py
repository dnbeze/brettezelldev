from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #import django user sign up form
from django.contrib.auth.models import User
# Create your views here.

def signupuser(request):
    #if method GET display signup user form - if post 
    if request.method == 'GET':
        return render(request, 'hello/signupuser.html', {'form':UserCreationForm()}) # importing UserCreation form is used here (UserCreationForm())

    else:
        #create new user 
        if request.POST['password1'] == request.POST['password2']: #check if passwords match
            User.objects.create_user(request.POST['username'], password=request.POST['password1']) #pass user.objects.create_user items in request.POST(dictionary)
        
        #tell users passwords didnt match


