from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import Register_AUTH_Form
from django.contrib import messages
from affairs.models import Intake
from affairs.forms import Intake_Form
# Create your views here.
def log_in (request): 
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username ," --- ",password)
        user = authenticate(request, username=username, password=password)
        request.session['username']=username
        if user is not None:
            print("found")
            login(request, user)
            request.user=user
            return redirect('/home')
        else:
            messages.success(request,"this username or password is wrong")
            return redirect('/loginAuth')
        
 
        # Return an 'invalid login' error message.
    print("hi")
    return render(request,'DjangoAuth/login.html',{})

def log_out (request):
    messages.success(request,"you logged out successfully")
    request.session['username']=None
    logout(request)
    return redirect ('/home')

def register_Auth(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home')
    else:
        form = UserCreationForm()
    return render(request,'DjangoAuth/register.html',{'form':form})

    
#add intake 

def add_intake(req):
    submitted=False
    if req.method=="GET" :
        # new form
        form=Intake_Form
        if 'submitted' in req.GET :
            # from the 2nd second request
            submitted=True
        return render (req,'IntakeFormForm.html',{'form':form,'submitted':submitted})
    else :
        #req is post data already in
        form=Intake_Form(req.POST)
        if form.is_valid():
            data=form.cleaned_data
            Intake.objects.create(name=data['name'],
             number=data['number'],start_date=data['start_date'],end_date=data['end_date'],manager=req.user)
            return HttpResponseRedirect('/add_intake?submitted=True')
        else :
            # to view errors
           return render (req,'IntakeFormForm.html',{'form':form,'submitted':submitted})
