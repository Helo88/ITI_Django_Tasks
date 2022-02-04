from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import Register_AUTH_Form
from django.contrib import messages
# Create your views here.
def log_in (request): 
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username ," --- ",password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("found")
            login(request, user)
            return redirect('/home')
        else:
            messages.success(request,"this username or password is wrong")
            return redirect('/loginAuth')
        
 
        # Return an 'invalid login' error message.
    print("hi")
    return render(request,'DjangoAuth/login.html',{})

def log_out (request):
    messages.success(request,"you logged out successfully")
    logout(request)
    return redirect ('/home')

def register_Auth(request):
    if request.method=="POST":
        form=Register_AUTH_Form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
        return redirect('/home')

    return render(request,'DjangoAuth/register.html',{'form':Register_AUTH_Form()})
    