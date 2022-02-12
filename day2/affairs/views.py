from ast import Sub
import json
from multiprocessing import Event
from re import sub, template
from unicodedata import name
from django import forms
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import  Students,Intake
from .forms import Student_Form,Intake_Form 
from django.views.generic import ListView

class IntakeList(ListView):
    template_name="tracks.html"
    model=Intake
    def get_query(self):
        return Intake.objects.all()
    
# Create your views here.
def home (request,students={}):
         print("req is ",students)
         #students=Students.objects.all()
         search=request.GET.get('search',None)
        #  print("sea",search)
         if search :
             students=Students.objects.all().filter(name=search)
         else :
             students=Students.objects.all()
         return  render(request,'home.html',{'students':students})
     

def login (request):
    context={}
    if(request.method=='GET'):
        context['students']=Students.objects.all()
        return render(request, 'login.html',context)
    else:
        #check for user and passs
        email=request.POST['email']
        password=request.POST['password']
        print('login data',email," -- ",password)
        #if correct
        allStudents=Students.objects.all()
        students= Students.objects.filter(email=email,password=password)
        
        if(len(students)>0):
            print(len(allStudents))
            return redirect('/home',{'students':allStudents})
            
                

        else:
            #else print errr statment
            context['errormsg']='incalid cred.'
            return render(request, 'login.html', context)

        
     
     
def register (req):
       context = {}
       if(req.method=='GET'):
            return  render(req,'register.html')
       else:
            print(req.POST)
            #cretae myuser
            Students.objects.create(name=req.POST['name'],address=req.POST['address'],
            email=req.POST['email'],password=req.POST['password'],confirm_password=req.POST.get('confirm_password'))
            students=Students.objects.all()
            return redirect('/login')

def delete (request,student_id):
    print("this is student_id",student_id)
    student=Students.objects.get(pk=student_id)
    student.delete()
    return redirect ('/home')

def update (request,student_id):
    student=Students.objects.get(pk=student_id)
    if(request.method=='GET'):
        #student=Students.objects.get(pk=student_id)
        return render (request,'form.html',{'student':student})
    else :
        
        print(request.POST['name'])
        student.name=request.POST['name']
        student.email=request.POST['email']
        student.address=request.POST['address']
        student.save()
        return redirect('/home')


def search (req):
    if req.method =="POST":
           searched=req.POST['searched']
           print("search  running is",searched)
           students=Students.objects.filter(name=searched)
           return  render(req,'searchResults.html',{'searched':searched,'students':students})
    else :
        pass
 

def add_student(req):
    submitted=False
    if req.method=="GET" :
        # new form
        form=Student_Form
        if 'submitted' in req.GET :
            # from the 2nd second request
            submitted=True
        return render (req,'studentModelForm.html',{'form':form,'submitted':submitted})
    else :
        #req is post data already in
        form=Student_Form(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_student?submitted=True')
        else :
           return render (req,'studentModelForm.html',{'form':form,'submitted':submitted})
        
        
        
