from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Register_AUTH_Form (UserCreationForm):
    class Meta ():
        model=User
        fields=['username','password1','password2']
         
        def __init__(self,*args):
            # super().__init__(*args)
            self.fields['username'].widget.attrs['class']='form-control'
            self.fields['password1'].widget.attrs['class']='form-control'
            self.fields['password2'].widget.attrs['class']='form-control'
                
             
    

