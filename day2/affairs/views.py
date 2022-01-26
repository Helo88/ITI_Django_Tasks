import json
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import Student, Students
# Create your views here.
def home (request):
         print("req is ",request)
         allStudents=Students.objects.all()
         return  render(request,'home.html',{'students':allStudents})
     

def login (request):
    context={}
    if(request.method=='GET'):
        context['students']=Students.objects.all()
        return render(request, 'login.html',context)
    else:
        #check for user and passs
        email=request.POST['email']
        password=request.POST['password']
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
            email=req.POST['email'],password=req.POST['password'])
            students=Students.objects.all()
            return redirect('/login')

def delete (request,student_id):
    print("this is student_id",student_id)
    student=Students.objects.get(pk=student_id)
    student.delete()
    return redirect ('/home')

def update (request,student_id):
    if(request.method=='GET'):
        #student=Students.objects.get(pk=student_id)
        return render (request,'form.html')
    else :
        student=Students.objects.get(pk=student_id)
        print(request.POST['name'])
        student.name=request.POST['name']
        student.email=request.POST['email']
        student.address=request.POST['address']
        student.save()
        return redirect('/home')