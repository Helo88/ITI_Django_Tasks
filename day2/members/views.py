from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
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
    