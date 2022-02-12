from django import forms
from django.forms import ModelForm
from .models import Intake, Students
import re 
class Student_Form(ModelForm):
      class Meta ():
        model=Students
        fields="__all__"
        labels={
            'name':'',
            'email':'',
            'address':'',
            'password':'',
            'confirm_password':''
             
            
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter address'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter password'}),
            'confirm_password':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter password again'}),
        }
        
      def clean(self):
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            password_regex=r'^.*(?=.{8,10})(?=.*[a-zA-Z])(?=.*?[A-Z])(?=.*\d)[a-zA-Z0-9!@£$%^&*()_+={}?:~\[\]]+$'
            data = self.cleaned_data
            print(data)
            if not re.fullmatch(email_regex, data['email'] ):
                raise forms.ValidationError('email format is wrong')
            if not re.fullmatch(password_regex,data['password']) or not re.fullmatch(password_regex,data['confirm_password']):
                raise forms.ValidationError('Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character') 
            if data['password'] !=  data['confirm_password'] :
                raise forms.ValidationError('passwords don\'t match')



class Intake_Form(forms.Form):
    name=forms.CharField(min_length=5,max_length=15,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Intake Name'}))
    number=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Intake Number'}))
    start_date=forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1',
            'placeholder':'Enter Intake Start Date'
        }))
    end_date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Intake End Date','class':'form-control datetimepicker-input','data-target':'#datetimepicker1'}))
    #students:forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Students'}))
   
       
            
        
